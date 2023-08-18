from pprint import pprint
N, M, V = map(int, input().split())

arr = [[0] * (N + 1) for _ in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1
pprint(arr)
visited = [0] * (N+1)

def DFS(start):
    print(start)
    for i in range(M):
        if visited[i] == 1:
            continue
        if arr[start][i] == 1:
            visited[i] = 1
            DFS(i)
DFS(V)