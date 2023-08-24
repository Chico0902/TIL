from collections import deque
from math import ceil
T = int(input())

def suffle(n,m):
    while n:
        hap.append(n.popleft())
        if not m:
            break
        hap.append(m.popleft())


for tc in range(1, T + 1):
    hap = []
    N = int(input())
    o_list = list(input().split())
    S = ceil(N/2)
    deq1 = o_list[:S]
    deq2 = o_list[S:]
    one = deque(deq1)
    two = deque(deq2)
    suffle(one, two)
    print(f'#{tc}', *hap)
