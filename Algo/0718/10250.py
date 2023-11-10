T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    bang = (N%H*100)+((N//H)+1)
    if N%H !=  0 :
        print(bang)
    if N%H == 0 :
        print(H*100+(N//H))
        