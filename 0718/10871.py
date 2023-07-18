a, b = map(int, input().split())
X = list(map(int,input().split()))
for i in range(a):
    if X[i]<b :
        print(X[i], end = " ")