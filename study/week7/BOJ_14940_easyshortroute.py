from pprint import pprint
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def BFS():
    global cnt
    while q:
        a = q.popleft()
        
        for k in range(4):
            ny = a[0]+dy[k]
            nx = a[1]+dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] == 1 and  visited[ny][nx] == -1:
                    visited[ny][nx]  = visited[a[0]][a[1]] +1
                    now = ny,nx
                    q.append(now)
                    # print(visited)
        # cnt += 1

N, M = map(int, input().split())

arr = [list(map(int, input().split()))for _ in range(N)]
visited = [[-1]*(M) for _ in range(N)]
# cnt = 1

for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                q = deque()
                start = i,j
                q.append(start)
                BFS()
for i in range(N):
    print(*visited[i])