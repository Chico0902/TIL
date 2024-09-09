from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
tower = list(map(int, input().split()))
ans_list = [0]*N
q = deque()
q.append((N-1,tower.pop()))

for i in range(1,N):
    while q:
        if tower[-1] >= q[0][1]:
            ans_list[q[0][0]] = N-i
            q.popleft()
        else:
            break
    q.appendleft((N-i-1,tower.pop()))
    # print(ans_list,'ans')


print(*ans_list)