N = int(input())
DP = [False] * 1001

DP[1] = True
DP[2] = False
DP[3] = True
DP[4] = False
DP[5] = False
DP[6] = False
DP[7] = False
if N >= 8:
    for i in range(8, N+1):
        if not DP[i-1] and not DP[i-3] and not DP[i-4]:
            DP[i] = True
    # elif DP[i-1] and DP[i-3] and DP[i-4]:
    #     DP[i] = False
        else:
            DP[i] = False
if DP[N]:
    print('CY')
else:
    print('SK')