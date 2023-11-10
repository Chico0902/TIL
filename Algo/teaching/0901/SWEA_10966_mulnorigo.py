# 룩업 테이블 : 미리 계산된 값을 저장해 놓은 테이블(리스트) -> 계산 시간을 줄이고, 코드를 간결하게 하기위해

'''
#파이프 모양별로 4방향 연결 가능 여부 나타내는 리스트 -> [상, 하, 좌, 우]
pipe = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]]
#상, 하, 좌, 우 이동을 위한 dir
di, dj = [-1, 1, 0, 0], [0, 0, 1, 1]
#상하, 좌우 매칭하기 위한 리스트(상-하, 좌-우)
opp = [1, 0, 3, 2]
'''

from collections import deque
dir = [(0, -1), (-1, 0), (0, 1), (1, 0)]
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) #격자의 크기
    check = [[-1 for _ in range(M)] for _ in range(N)] #최단 거리를 저장할 리스트
    q = deque() #bfs 를 위한 큐 생성
    for i in range(N):
        t = input() #격자를 입력 받으면서
        for j in range(M):
            if t[j] == 'W': #W를 발견하면
                q.append((i, j)) # 큐에 추가하고
                check[i][j] = 0 #거리를 0으로 설정
    result = 0
    while q:
        x, y = q.popleft() #큐에서 하나를 꺼내고, 상하 좌우로 이동
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            #이동이 가능하고, 아직 방문하지 않았다면
            if 0 <= nx < N and 0 <= ny < M and check[nx][ny] == -1:
                q.append((nx, ny)) # 1. 큐에 추가
                check[nx][ny] = check[x][y] + 1 #2. 거리 갱신
                result += check[nx][ny] #3. result 갱신
    print(f'#{tc} {result}')