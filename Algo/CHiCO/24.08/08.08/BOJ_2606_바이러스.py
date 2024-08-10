import sys
from collections import defaultdict, deque

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

compu = defaultdict(list)
index = 2

for _ in range(M):
    s = int(data[index])
    e = int(data[index + 1])
    compu[s].append(e)
    compu[e].append(s)
    index += 2

def bfs(start):
    visited = [0]*N
    q = deque([start])
    visited[start] = 1
    cnt = 0

    while q:
        now = q.popleft()
        for i in compu[now]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)
                cnt += 1
    return cnt

ans = bfs(1)

print(ans)