from pprint import pprint
N, M, V = map(int, input().split())

arr = [[0] * (N + 1) for _ in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1
visited = [0] * (N+1)

def DFS(start):
    print(start, end=' ')
    visited[start] = 1
    for i in range(N + 1):
        if visited[i] == 1:
            continue
        if arr[start][i] == 1:
            DFS(i)
            
DFS(V)

# def DFS(start):
#     print(start)
#     visited[start] = 1
#     for i in range(N+1):
#         if arr[start][i] == 1 and visited[i] == 0:
#             DFS(i)
# DFS(V)

print()
from collections import deque

def BFS(start):
    q = deque()
    visited2 = [0] * (N + 1)
    q.append(start)
    visited2[start] = 1
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in range(N + 1):
            if arr[now][i] == 1 and visited2[i] == 0:
                q.append(i)
                visited2[i] = 1

BFS(V)


