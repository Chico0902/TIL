T = int(input())

for tc in range(1, 1+T):
    N , M = list(map(int, input().split()))
    hwa_moogae = list(map(int, input().split()))
    jukjae = list(map(int, input().split()))

    a = sorted(hwa_moogae)
    b = sorted(jukjae)
    cnt = 0

    while a and b:
        c_a = a.pop()
        c_b = b.pop()
        while a:
            if c_a > c_b:
                c_a = a.pop()
            elif c_a <= c_b:
                break
        if c_a <= c_b:
            cnt += c_a

    print(f'#{tc} {cnt}')