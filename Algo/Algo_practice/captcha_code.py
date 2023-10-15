from collections import deque

T = int(input())
for tc in range(1, 1+T):
    N, K = map(int, input().split())
    Sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))

    sq = deque(Sample)
    pq = deque(passcode)

    for i in range(N):
        comp = sq.popleft()
        if comp == pq[0]:
            pq.popleft()
        if not pq:
            print(f'#{tc} 1')
            break
    else:
        print(f'#{tc} 0')
