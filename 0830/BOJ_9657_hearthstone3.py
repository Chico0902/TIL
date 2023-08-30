N = int(input())

DP = [False] * (N + 2)
DP[1] = False
DP[2] = True
DP[3] = False
DP[4] = False
if N >= 5:
    for i in range(5, N + 1):
        if not DP[i - 1] and not DP[i - 3] and not DP[i - 4]:
            DP[i] = True
if N == 1 or N == 3 or N == 4:
    print('SK')
elif not DP[N]:
    print('SK')
elif N == 2:
    print('CY')
else:
    print('CY')

#
# N = int(input())
#
# if N % 7 == 2 or N % 7 == 0:
#     print('CY')
# else:
#     print('SK')
