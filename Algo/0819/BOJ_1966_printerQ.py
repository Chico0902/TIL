from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        arr[i] = (arr[i], i)
    q = deque(arr)
    X = q[M]
    cnt = 1
    while q:
        if q.index(X) == 0 and X == max(q):
            print(cnt)
            break
        elif q[0] == max(q) and q[0] != X:
            q.popleft()
            cnt += 1
        elif q[0] != max(q):
            q.append(q.popleft())
            
from collections import deque

num_list = deque([(1,0), (2,1), (3,2)])
for _ in range(3):
    print(num_list)
    num_list.rotate(-1)