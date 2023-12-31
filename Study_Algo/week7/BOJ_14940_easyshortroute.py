from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs():
    global cnt
    while q:
        a = q.popleft()
        for k in range(4):
            ny = a[0]+dy[k]
            nx = a[1]+dx[k]
            if 0 <= ny < N and 0 <= nx < M:
                if arr[ny][nx] == 1 and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[a[0]][a[1]] + 1
                    now = ny, nx
                    q.append(now)


N, M = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            visited[i][j] = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            visited[i][j] = 0
            q = deque()
            start = i, j
            q.append(start)
            bfs()
for i in range(N):
    print(*visited[i])