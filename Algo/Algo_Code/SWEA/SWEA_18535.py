dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
T = int(input())
for tc in range(1, 1+T):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    for i in range(N):
        for j in range(N):
            sum = 0
            sum += arr[i][j]
            for k in range(4):
                for l in range(1, 1+P):
                    ny = i+dy[k]*l
                    nx = j+dx[k]*l
                    if 0 <= ny < N and 0 <= nx < N:
                        sum += arr[ny][nx]
            if sum > max_sum:
                max_sum = sum
    print(f'#{tc} {max_sum}')
