N = int(input())
arr = []
for _ in range(N):
    now = input()
    arr.append(now)
    if now[::-1] in arr:
        ans = len(now)
        print(ans, now[ans//2])


