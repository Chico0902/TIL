# 콜라츠 추측
N = int(input())

def solve(num, cnt):
    # 재귀함수 종료
    if num == 1:
        print(cnt)
        return
    # 어떤수가 짝수라면
    if num % 2 ==0:
        solve(num / 2, cnt + 1)
    # 어떤수가 홀수라면
    else:
        solve((num*3) + 1, cnt + 1)
solve(N, 0)