from pprint import pprint
from collections import deque
N, M = map(int, input().split())

arr = [list(map(int, input().split()))for _ in range(n)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            x, y = i, j
