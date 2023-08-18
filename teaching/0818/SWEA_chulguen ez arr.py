from collections import deque
N, M = map(int, input().split())
arr = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    arr[A][B] = 1
    arr[B][A] = 1 #양방향 그래프
R, K = map(int, input().split())
cnt = 0

def bfs(node):
    global cnt
    q = deque()
    q.append(node)
    visited[node] = 1
    while q:
        now = q.popleft()
        if visited[now] - 1 <= K: #탐색 깊이가 K이하면 카운트 증가
            cnt += 1
        if visited[now] - 1 > K:
            break
        for i in range(1, N+1):
            if arr[now][i] == 0: #연결되지 않은 노드는 건너뜀
                continue
            if visited[i] > 0 : #이미 방문한 노드 건너뜀
                continue
            visited[i] = visited[now] + 1
            q.append(i)
bfs(R)
print(cnt)