from collections import deque

T = int(input())
q = deque()
dy = [-1, 0, 1, 0]
dx = [0, 1, 0 ,-1]

def BFS(start):
    visited = [[0] * 5 for _ in range(5)]
    q = [start]
    a = start[0]
    b = start[1]
    while q:
        now = q.pop()
        for k in range(4):
            if 0 <= a + dy[k] < N and 0 <= b+dy[k] < N:
                if miro[a+dy[k]][b+dx[k]] == 0:
                    visited[a+dy[k]][b+dx[k]] = 
    
for tc in range(1, 1+T):
    N = int(input())
    miro = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                start = (i, j)

