from collections import deque

N = int(input())
Jum = deque()
min_X = 9999999999
max_X = -999999999
min_Y = 999999999
max_Y = -99999999999
flag = 1
for i in range(N):
    X,Y = map(int, input().split())
    if X < min_X:
        min_X = X
    elif X > max_X:
        max_X = X
    if Y < min_Y:
        min_Y = Y
    elif Y > max_Y:
        max_Y = Y
    Jum.append((X,Y))
# print(max_X,min_X,max_Y,min_Y)
while Jum:
    now = Jum.popleft()
    if now[0] != min_X and now[0] != max_X:        
        if min_Y < now[1] < max_Y:
            flag = 0
        if max_X - min_X != max_Y - min_Y:
            flag = 0
        else:
            continue
    else:
        continue
    
if flag:
    print(max((max_X-min_X,max_Y-min_Y)))
else:
    print(-1)

# --------------------------------------------



