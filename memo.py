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