from pprint import pprint

T = int(input())

dy = [0, -1]
dx = [-1, 0]

for tc in range(T):
    M, N, K = map(int, input().split())
    arr = [([0] * M) for _ in range(N)]
    cnt = 0
    for _ in range(K):
        y, x = map(int, input().split())
        arr[x][y] = 1
    pprint(arr)
    for i in range(N):
        for j in range(M):
            flag = True
            for k in range(2):
                if i == 0 and j == 0:
                    if arr[i][j] == 1:
                        cnt += 1
                if arr[i][j] == 1:
                    if 0 <= i + dy[k] < N and 0 <= j + dx[k] < M:
                        if arr[i + dy[k]][j + dx[k]] == 1:
                            flag = False
                            if flag:
                                cnt += 1
    print(cnt)