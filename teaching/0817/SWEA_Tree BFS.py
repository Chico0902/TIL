from collections import deque
arr = [
    [0,1,0,0,1,0],
    [0,0,1,0,0,1],
    [0,0,0,1,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]
k = int(input())
def bfs(now):
    q = deque()
    q.append(now) #시작 노드를 큐에 추가
    while q:
        now = q.popleft()# 큐에서 하나의 노드를 꺼낸후 출력
        print(now, end=' ')
        for i in range(6): # 현재 노드와 연결된 모든 노드를 확인
            if arr[now][i] == 1: # 현재 노드와 1번째 노드가 연결되어 있다면
                q.append(i) # i번째 노드를 큐에 추가
bfs(k) #bfs(너비우선탐색) k 부터 시작