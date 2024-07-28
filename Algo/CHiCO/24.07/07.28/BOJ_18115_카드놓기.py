from collections import deque

N = int(input())
arr = deque(map(int, input().split()))

answer_list = deque()
idx = 0

while arr:
    now = arr.pop()
    if now == 1:
        answer_list.appendleft(idx+1)
        idx += 1
    elif now == 2:
        answer_list.insert(1, idx+1)
        idx += 1
    else:
        answer_list.append(idx+1)
        idx += 1

print(*answer_list)