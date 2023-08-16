# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#
# 풀어보려고했으나
# N = int(input())
# from itertools import product
# my_list = [1, 2]
# new_list = []
# for i in range(1, N+1):
#     A = list(product(my_list, repeat = i))
#     if sum(A) == 5:
#         new_list.append(my_list)

#-------------------------------------------
# 재귀함수 1. 자기자신을 호출 2. 종료조건을 반드시 포함
# F1 = 1, F2 = 3, F3 = 5, F4 = 11
# 피보나치 수열 Fn = Fn-1 + Fn-2 와 유사하게 접근 -> Fn = Fn-1 + (2 * Fn-2)

def func(n):
    if n % 10 == 0:
        #재귀함수의 종료조건
        if n == 10:
            return 1
        elif n == 20:
            return 3
        #Fn = Fn-1 + (2* Fn-2)
        else : #n이 30이상
            return func(n-10) +(2 * func(n-20))

T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    num = func(n)
    print(f'#{tc} {num}')