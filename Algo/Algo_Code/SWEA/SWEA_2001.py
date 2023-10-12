def flyout(y,x,M):
    global cnt
    for i in range(M):
        for j in range(M):
            cnt += arr[y+i][x+j]
    return cnt


T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    for i in range(N-(M-1)):
        for j in range(N-(M-1)):
            cnt = 0
            now = flyout(i,j,M)
            if max_cnt < now:
                max_cnt = now
    print(f'#{tc} {max_cnt}')

