from collections import deque
N, K = map(int, input().split())
student = deque()
nam = []
yeo = []
for _ in range(N):
    S, Y = map(int, input().split())
    student.append([S, Y])
while student:
    now = student.pop()
    if now[0] == 0:
        yeo.append(now)
    elif now[0] == 1:
        nam.append(now)

l_y = len(yeo)
l_n = len(nam)
y_1 = []
y_2 = []
y_3 = []
y_4 = []
y_5 = []
y_6 = []
n_1 = []
n_2 = []
n_3 = []
n_4 = []
n_5 = []
n_6 = []

for i in range(l_y):
    if yeo[i][1] == 1:
        y_1.append(yeo[i][1])
    elif yeo[i][1] == 2:
        y_2.append(yeo[i][1])
    elif yeo[i][1] == 3:
        y_3.append(yeo[i][1])
    elif yeo[i][1] == 4:
        y_4.append(yeo[i][1])
    elif yeo[i][1] == 5:
        y_5.append(yeo[i][1])
    elif yeo[i][1] == 6:
        y_6.append(yeo[i][1])
for i in range(l_n):
    if nam[i][1] == 1:
        n_1.append(nam[i][1])
    elif nam[i][1] == 2:
        n_2.append(nam[i][1])
    elif nam[i][1] == 3:
        n_3.append(nam[i][1])
    elif nam[i][1] == 4:
        n_4.append(nam[i][1])
    elif nam[i][1] == 5:
        n_5.append(nam[i][1])
    elif nam[i][1] == 6:
        n_6.append(nam[i][1])
