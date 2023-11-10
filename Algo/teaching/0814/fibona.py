# 재귀는 시간초과
# import sys
# input = sys.stdin.readline
# def fibo(i):
#     if i == 0:
#         return [1, 0]
#     elif i == 1:
#         return [0, 1]
#     elif i == 2:
#         return [1, 1]
#     else:
#         return [fibo(i-1)[0] + fibo(i-2)[0], fibo(i-1)[1] + fibo(i-2)[1]]
# T = int(input())
#
# for _ in range(T):
#     a = int(input())
#     print(*fibo(a))




T = int(input())
for k in range(T):
    n = int(input())
    fb = [[1, 0], [0, 1]]*(n+1)
    for i in range(2, n+1):
        fb[i] = [fb[i-1][0] + fb[i-2][0], fb[i-1][1] + fb[i-2][1]]
    print(*fb[n])
