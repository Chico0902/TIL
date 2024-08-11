A, K = map(int, input().split())

DP = [0] * (K+1)

DP[A] = 1

while A != K:
    if 2*A <= K:
        DP[2*A] = DP[A] + 1
    if DP[A+1] != 0:
        DP[A+1] = min(DP[A] + 1, DP[A+1])
    else:
        DP[A+1] = DP[A] + 1
    
    A += 1

print(DP[K]-1)