T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split()))for _ in range(N)]
    result = 0
    for i in range(N):
        cnt = 0
        for j in range(N): # 각 행을 검사
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == N -1: #현재 위치가 0이거나, 마지막 열인 경우
                if cnt == K:
                    result += 1
                cnt = 0
    for i in range(N):
        cnt = 0
        for j in range(N): # 각 열을 검사
            if puzzle[j][i] == 1:
                cnt += 1
            if puzzle[j][i] == 0 or j == N -1: #현재 위치가 0이거나, 마지막 행인 경우
                if cnt == K:
                    result += 1
                cnt = 0
    print(f'#{tc} {result}')