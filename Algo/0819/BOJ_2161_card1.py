from collections import deque
N = int(input())
arr = list(range(1, 1+N))
q = deque(arr)

while len(q) > 1:
    a = q.popleft()
    print(a,end=' ')
    q.append(q.popleft())    
print(*q)