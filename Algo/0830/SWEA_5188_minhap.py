# 완전탐색 : 문제 해결을 위해 가능한 모든 경우의 수를 탐색하는 방법
#: stack, queue, DFS ,BFS, 백트래킹, 분할정복, 시뮬레이션(사과먹기, 농사)
dir = [(0, 1), (1, 0)]

def dfs(x, y, sum_v):   # x, y는 현재 위치, sum_v는 현재까지의 합계
    global result
    # 가지치기: 불필요한 경로를 차단 -> 조건에 맞지 않으면 탐색하지 않는다.
    if sum_v >= result:
        return
    # 목표 지점에 도착한 경우
    if x == N-1 and y == N-1:
        if sum_v < result:
            result = sum_v
        return
    for dx, dy in dir:
        nx, ny = x+dx, y+dy
        if -1 < nx < N and -1 < ny < N:
            dfs(nx, ny, sum_v + arr[nx][ny])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')   # 무한대 표현, 음의 무한대: -float('inf')
    dfs(0, 0, arr[0][0])
    print(f'#{tc} {result}')