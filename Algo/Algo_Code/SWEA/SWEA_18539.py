T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_space = 0
    print(arr)
    for i in range(N):
        for j in range(N):
            now = arr[i][j]
            for k in range(N-i,N):
                for l in range(N-j,N):
                    if arr[k][l] == now:
                        space = (k-i)*(l-j)
                        if max_space < space:
                            max_space = space
    print(f'#{tc} {max_space}')