from pprint import pprint
N, M, K = map(int,input().split())

arr = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input(). split())
    arr[a][b] = 1
    arr[b][a] = 1
visited = [0] * (N + 1)
def DFS(start):
     now = start
     visited[now] = 1
     print(now, end=' ') 
     for i in range(1,N+1):        
        if arr[now][i] == 1 and not visited[i] == 1:
            visited[i] = 1
            DFS(i)
DFS(K)
print()

from collections import deque
n_visited = [0] * (N + 1)
q = deque()
def BFS(start):
    q.append(start)
    now = start
    n_visited[start] = 1
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in range(1, N + 1):
            if n_visited[i] == 0 and arr[now][i] == 1:
                q.append(i)
                n_visited[i] = 1
BFS(K)

