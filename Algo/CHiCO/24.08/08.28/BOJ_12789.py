from collections import deque

N = int(input())
arr = deque(map(int, input().split()))

cnt = 1
stack = []

for _ in range(N):
    now = arr.popleft()
    if cnt == now:
        cnt += 1
        while True:
            if stack:
                if stack[-1] == cnt:
                    stack.pop()
                    cnt += 1
                else:
                    break
            else:
                break
    else:
        stack.append(now)


if stack:
    print('Sad')
else:
    print('Nice')

### 이게 더 시간 많이잡아먹는데?

# while arr:
#     stack.append(arr.popleft())
#     while stack and stack[-1] == cnt:
#         stack.pop()
#         cnt += 1
# print('Sad' if stack else 'Nice')