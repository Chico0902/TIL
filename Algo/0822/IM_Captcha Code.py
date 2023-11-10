from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    Sample = list(input().split())
    PassCode = list(input().split())
    S = deque(Sample)
    P = deque(PassCode)

    for i in range(N):
        now = S.popleft()
        if P:
            if now == P[0]:
                P.popleft()
    if P:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')
