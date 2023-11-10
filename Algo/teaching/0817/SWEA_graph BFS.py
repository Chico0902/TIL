from collections import deque
arr = [
    [0,0,0,0,1,0],
    [1,0,1,0,0,1],
    [1,0,0,1,0,0],
    [1,1,0,0,0,0],
    [0,1,0,1,0,1],
    [0,0,1,1,0,0,]
]

s = int(input())
used = [0]*6
def bfs(now):
    q = deque()
    q.append(now)
    while q:
        now = q.popleft()
        print(now)
        for i in range(6):
            if used[i] == 1: continue #이미 방문한 노드는 건너뛰기
            if arr[now][i] == 1:
                used[i] = 1 # i번째 노드를 방문했다고 체크
                q.append(i)
used[s] = 1 #시작 노드 방문
bfs(s)