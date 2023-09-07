T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    cnt = 0
    for i in range(N):
            cnt += int(arr[i][N//2])
            if i <= N//2:
                for k in range(i+1):
                    if k != 0:
                        cnt += int(arr[i][N//2+k])
                        cnt += int(arr[i][N//2-k])
            elif i > N//2:
                for k in range(N-i):
                    if k !=0:
                        cnt += int(arr[i][N//2-k])
                        cnt += int(arr[i][N//2+k])
    print(f'#{tc} {cnt}')