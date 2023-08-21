from collections import deque
N = int(input())
arr = list(range(1, N+1))
q = deque(arr)
def hi():
    q.popleft()
    q.append(q.popleft())
while len(q) > 1:
    hi()

print(*q)
