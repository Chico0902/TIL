import sys
N, M = map(int,sys.stdin.readline().split())
DJ = []
BJ = []
DBJ = []
for _ in range(N):
    DJ.append(sys.stdin.readline())
for _ in range(M):
    BJ.append(sys.stdin.readline())
for i in DJ:
    if i in BJ:
        DBJ.append(i)
ans = sorted(DBJ)
print(len(ans))
for i in range(len(ans)):
    print(ans[i])