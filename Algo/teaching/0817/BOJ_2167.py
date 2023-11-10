import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]
K = int(input())

for _ in range(K):
    i,j,x,y = map(int, input().split())
    cnt = 0
    for di in range(x-i+1):
        for dj in range(y-j+1):
            ni, nj = i + di, j + dj
            cnt += arr[ni-1][nj-1]
    print(cnt)