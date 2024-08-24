from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
arr = []
visited = [[0]*N for _ in range(N)]
m_dict = defaultdict(list)

for _ in range(N):
    arr.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            m_dict[i].append(j)

for start in range(N):
    stack = [start]
    while stack:
        now = stack.pop()
        for i in m_dict[now]:
            if not visited[start][i]:
                visited[start][i] = 1
                stack.append(i)


for row in visited:
    print(" ".join(map(str, row)))


# 플로이드 워셜이라는 알고리즘

import sys
input = sys.stdin.readline

N = int(input())
arr = []

# 인접 행렬 입력 받기
for _ in range(N):
    arr.append(list(map(int, input().split())))

# 플로이드-워셜 알고리즘 적용
for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][k] and arr[k][j]:
                arr[i][j] = 1

# 결과 출력
for row in arr:
    print(" ".join(map(str, row)))
