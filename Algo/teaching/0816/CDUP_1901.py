n = int(input())
cnt = 1
def nu(n):
    global cnt
    print(cnt)
    if cnt < n:
        cnt += 1
        nu(n)
nu(n)