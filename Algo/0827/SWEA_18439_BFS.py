from collections import deque
arr = [[0,0,0,0,1,0], [1,0,1,0,0,1],[1,0,0,1,0,0,],[1,1,0,0,0,0,],[0,1,0,1,0,1],[0,0,1,1,0,0]]
N = int(input())

visited = [0] * (len(arr) + 1)

q = deque()
q.append(N)
visited[N] = 1
while q:
    now = q.popleft()    
    print(now)
    for i in range(6):
        if arr[now][i] == 1 and not visited[i] == 1:
            q.append(i)
            visited[i] = 1
            
