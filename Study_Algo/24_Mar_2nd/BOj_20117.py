N = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
if N % 2 == 0:
    for i in range(1,(N//2)+1):
        # print(i)
        ans += arr[-i]*2
else:
    for i in range(1,(N//2)+1):
        ans += arr[-i]*2
    ans += arr[(N//2)]


print(ans)