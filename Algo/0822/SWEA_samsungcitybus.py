T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    busstop = [0] * 5001
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            busstop[i] += 1
    P = int(input())
    ans = []
    for i in range(P):
        ans.append(busstop[int(input())])

    print(f'#{tc}', *ans)