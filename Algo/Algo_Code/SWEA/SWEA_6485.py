T = int(input())
for tc in range(1, 1+T):
    busstop = [0] * 5001
    N = int(input())
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            busstop[i] += 1
    P = int(input())
    ans = []
    for _ in range(P):
        C = int(input())
        ans.append(busstop[C])
    print(f'#{tc}', *ans)
