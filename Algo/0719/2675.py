T = int(input())
for i in range(T):
    a ,b = (input().split())
    a = int(a)
    b = list(b)
    for x in range(len(b)):
        print(a*b[x], end="")