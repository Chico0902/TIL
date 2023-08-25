from collections import deque

N, M = int(input())
miro = [list(map(int, input())) for _ in range(N)]
visited = [[0]* N for _ in range(M)]
distance = [[0] * N for _ in range(M)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0,-1]

def BFS():
    q = deque()
    start = (0, 0)
    cnt = 1
    q.append(start)
    visited[start[0]][start[1]] = 1
    distance[start[0]][start[1]] = 1
    while q:
        now = q.popleft()
        if now[0] == N-1 and now[1] == M-1:
            break
        else:
            cnt += 1
            for i in range(4):


