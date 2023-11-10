def check(num):
    num = str(num)
    for i in range(len(num) - 1):  # 각 자릿수 확인
        if num[i] > num[i+1]:  # 현재 자릿수가 다음 수보다 크면 False 리턴
            return False
    return True

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    result = 0  # 단조 증가하는 수의 최대값

    for i in range(N-1):
        for j in range(i+1, N):  # 두번째 정수 선택
            number = nums[i] * nums[j]
            if check(number):
                result = max(result, number)  # 단조 증가 수라면 최댓값 전환
        if result == 0:  # 단조 증가 수가 없다면
            result = -1

    print(f'#{tc} {result}')