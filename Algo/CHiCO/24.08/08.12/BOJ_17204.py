N, K = map(int, input().split())

arr = [0]
for _ in range(N):
    arr.append((int(input()))+1)

visited = [0]* (N+1)
visited[1] = 1
cnt = 0
now = 1
while True:
    cnt += 1
    pick = arr[now]
    if visited[pick]:
        ans = -1
        break
    if pick == K+1:
        ans = cnt
        break
    visited[pick] = 1
    now = pick

print(ans)

