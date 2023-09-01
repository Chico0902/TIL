T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    M_cnt = 0
    cnt = 0
    for i in range(N):
        for j in range(N):
            a = arr[i][j]

            for k in range(i, N):
                for l in range(j, N):
                    if arr[k][l] == a:
                        myun = (k-i+1) * (l-j+1)
                        if myun > M_cnt:
                            M_cnt = myun
                            cnt = 1
                        elif myun == M_cnt:
                            cnt += 1
    print(f'#{tc} {cnt}')