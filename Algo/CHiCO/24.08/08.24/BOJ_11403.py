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