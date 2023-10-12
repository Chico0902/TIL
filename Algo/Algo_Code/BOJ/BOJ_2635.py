X, Y =  map(int, input().split())
N = int(input())
R = [0]
C = [0]
for _ in range(N):
    RC, L = map(int, input().split())
    if RC == 0:
        R.append(L)
    else:
        C.append(L)
R.sort()
C.sort()
R.append(Y)
C.append(X)
max_R = []
max_C = []
for i in range(len(R)-1):
    max_R.append(R[i+1]-R[i])
for i in range(len(C)-1):
    max_C.append(C[i+1]-C[i])
max_X = max(max_R)
max_Y = max(max_C)
ans = max_X * max_Y
print(ans)