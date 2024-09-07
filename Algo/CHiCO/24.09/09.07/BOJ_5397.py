from collections import deque
import sys
input = sys.stdin.readline
T =  int(input().strip())
for _ in range(T):
    L_stack = []
    R_stack = deque()
    arr = list(input().strip())
    for i in arr:
        if i == '<' and L_stack:
            now = L_stack.pop()
            R_stack.appendleft(now)
        elif i == '>' and R_stack:
            now = R_stack.popleft()
            L_stack.append(now)
        elif i == '-' and L_stack:
            L_stack.pop()
        elif i != '<' and i != '>' and i != '-':
            L_stack.append(i)
    L_stack.extend(R_stack)
    print(*L_stack,sep='')