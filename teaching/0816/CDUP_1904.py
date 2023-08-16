a, b = map(int, input().split())
def jae(a,b):
    if a % 2 == 1:
        print(a, end=' ')
        if a < b:
            jae(a+1, b)
    elif a % 2 == 0:
        if a < b:
            jae(a+1, b)

jae(a,b)

