from itertools import product

# 입력 처리
N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 숫자 K의 원소들을 내림차순으로 정렬
arr.sort(reverse=True)

# N의 자리수 길이를 계산
length = len(str(N))

# 자리수별로 가능한 수를 찾기 위한 반복문
while length > 0:
    # 길이 'length'에 대한 모든 조합을 생성
    for num in product(arr, repeat=length):
        candidate = int(''.join(map(str, num)))
        if candidate <= N:
            print(candidate)
            exit()
    # 길이를 하나 줄여가며 반복
    length -= 1
