from collections import deque
def bfs(start, target):
    q = deque()
    q.append(start)#시작 위치 큐에 추가 인큐
    visited[start] = 1
    while q:
        now = q.popleft()
        for i in range(1, N+1):
            if arr[now][i] == 0: #연관이 없는 회원이면 무시
                continue
            if visited[i] == 1: #이미 방문한 회원 무시
                continue
            if i == target: #타켓 회원을 찾을 수 있으면 YES출력
                print('YES')
                return
            q.append(i) #연관된 회원을 큐에 추가
            visited[i] = 1 #방문한 것으로 표시
    print("NO")

N = int(input())
T = int(input())
arr = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N+1)
for _ in range(T):
    A, B = map(int, input().split())
    arr[A][B] = 1
    arr[B][A] = 1
coco = int(input())
target = int(input())
bfs(coco, target)