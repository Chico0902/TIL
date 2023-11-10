from collections import deque

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    d = deque(arr)
    while d[-1] > 0:
        for i in range(1, 6):
            a = d.popleft()-i
            if a <= 0:
                d.append(0)
                break
            elif a > 0:
                d.append(a)
    ans = list(d)
    print(f'#{tc}', *ans)