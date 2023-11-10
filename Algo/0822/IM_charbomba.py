dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

T = int(input())

for tc in range(1, 1 + T):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    anti_vir = []
    for i in range(N):
        for j in range(N):
            hap = []
            hap.append(arr[i][j])
            for k in range(4):
                for l in range(1, P+1):
                    if 0 <= (i + dy[k] * l) < N and 0 <= (j + dx[k] * l) <N:
                        hap.append(arr[i + dy[k] * l][j + dx[k] * l])
            anti_vir.append(sum(hap))
    ans = max(anti_vir)
    print(f'#{tc} {ans}')
