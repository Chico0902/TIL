# 분할정복 & 백트래킹

## 분할정복
 1. 분할 : 해결할 문제를 나눌 수 없을 때까지 여러개의 작은 부분으로 나눈다.
 2. 정복 : 나눈 작은 문제를 각각 해결한다.
 3. 통합 : 해결된 해답을 모은다. 
   
   ### 병합정렬
   1. 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종결과를 얻어냄.

## 퀵정렬
- 주어진 배열을 2개로 분할하고, 각각을 정렬한다.
    - 병합정렬과 다른점
     1. 기준아이템 중심으로, 이보다 작은것은 왼편, 큰것은 오른편에 위치
     2. 각 부분 정렬이 끝난 후, 퀵정렬은 '병합'이라는 후처리 과정이 필요하지 않음


### 이진검색 - 반복문
```

arr = [2, 4, 7, 9, 11, 19, 23]

arr.sort()

def binarySearch(target):
    low = 0
    high = len(arr)-1

    # low > high 라면 데이터를 못찾은 경우
    while low <= hign:
        mid = (low + high) // 2

        # 1. 가운데 값이 정다인 경우
        if arr[mid] == target:
            return mid

        # 2. 가운데 값이 정답보다 작은 경우
        elif arr[mid] < target:
            low = mid + 1
        # 3. 가운데 값이 정답보다 큰 경우
        else:
            high = mid - 1

    return "해당 데이터는 없습니다."

print(f'9 = {binarySearch(9)}')
```
### 이진검색 - 재귀호출 활용

```
arr = [2, 4, 7, 9, 11, 19, 23]

arr.sort()

def binarySearch(low, high,target):
    # 기저 조건 : 언제까지 재귀호출을 반복할 것인가?
    if low > high : 
        return -1
    
    mid = (low + high) // 2

    # 1. 가운데 값이 정답인 경우
    if target == arr[mid]:
        return mid
    # 2. 가운데 값이 정답보다 작은 경우
    elif arr[mid] < target:
        return binarySearch(mid + 1, high, target)
    # 3. 가운데 값이 정답보다 큰 경우
    else:
        return binarySearch(low, mid-1 , target)
```