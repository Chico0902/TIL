n = int(input())


def hap(n):
    if n == 1:
        return 1
    if n > 1:
        return n + hap(n-1)


print(hap(n))