import sys
sys.setrecursionlimit(10**6)
N, M ,R = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [0]*(N+1)
result = []
cnt = 0

def DFS(start):
    global cnt
    now = start
    cnt += 1
    visited[now] = cnt
    for i in range(N):
        if i in arr[now] and not visited[i]:
            visited[i] = 1
            DFS(i)



for i in range(N):
    a, b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)


DFS(R)
print(*visited[1:],sep='\n')

