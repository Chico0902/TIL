n = int(input())
cnt = n
def nu(n):
    global cnt
    print(cnt)
    if cnt > 1:
        cnt -= 1
        nu(n)
nu(n)