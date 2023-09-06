def DFS(N):
    visited = [0]*(N+1)
    now = N
    visited[now] = 1
    for i in range(N+1):
        if arr[now][i] == 1 and not visited[i] == 1:
            visited[i] = 1
            DFS(i)


N, M = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    arr[u][v] = 1
