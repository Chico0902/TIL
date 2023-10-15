T = int(input())
for tc in  range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    max_arr = 0
    for i in range(N):
        for j in range(N):
            now = arr[i][j]
            for k in range(N-i):
                for l in range(N-j):
                    n_now = arr[i+k][j+l]
                    if now == n_now:
                        sum_arr = (k+1) * (l+1)
                        if sum_arr > max_arr:
                            max_arr = sum_arr
                            cnt = 1
                        elif sum_arr == max_arr:
                            cnt += 1
    print(f'# {tc} {cnt}')
