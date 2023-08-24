# 오목판정
def omok():
    dy = [1, 0, 1, -1]  # 네 방향(오른쪽, 아래, 오른쪽 아래 대각선, 왼쪽 아래 대각선)
    dx = [0, 1, 1, 1]
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 'o':
                for dir in range(4):    # 돌이 놓여져 있다면 네 방향 검사
                    ny = y
                    nx = x
                    cnt = 0
                    while 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == 'o':
                        cnt += 1
                        ny += dy[dir]   # 다음 위치로 이동
                        nx += dx[dir]
                    if cnt >= 5:
                        return 'YES'
    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    print(arr)
    print(f'#{tc} {omok()}')