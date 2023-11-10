import math
T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N+1)]
    hy = []
    hx = []
    D = 0
    x = 0
    y = 0
    for i in range(N+1):
        for j in range(N+1):
            if arr[i][j] == 2:
                y, x = i, j
    for i in range(N+1):
        for j in range(N+1):
            if arr[i][j] == 1:
                hy.append(i)
                hx.append(j)
    for i in range(len(hy)):
        now = (hy[i] - y) ** 2 + (hx[i] - x) ** 2
        if now > D:
            D = now
    print(f'#{tc} {math.ceil(math.sqrt(D))}')
