from collections import deque

arr = deque(input())
A = []
B = []
while arr:
    if arr[0] not in A:
        A.append(arr.popleft())
    elif arr[0] in A:
        now = arr.popleft()
        B.append(now)
        A.remove(now)
if not A:
    B = sorted(B)
    ans = B+B[::-1]
    print(*ans, sep='')
elif len(A) == 1:
    B = sorted(B)
    ans = B+A+B[::-1]
    print(*ans, sep='')
elif len(A) > 1:
    print("I'm Sorry Hansoo")

