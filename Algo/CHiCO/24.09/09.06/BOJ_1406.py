from collections import deque
import sys
input = sys.stdin.readline
L_Stack = list(input().strip())
M = int(input())
R_Stack = deque()

for _ in range(M):
    cmd = input().strip()
    if cmd.startswith('P'):
        L_Stack.append(cmd[2])
    elif cmd == "L":
        if L_Stack:
            now = L_Stack.pop()
            R_Stack.appendleft(now)
    elif cmd == "D":
        if R_Stack:
            now = R_Stack.popleft()
            L_Stack.append(now)
    elif cmd == "B" and L_Stack:
        L_Stack.pop()

L_Stack.extend(R_Stack)
print(*L_Stack,sep="")