T = int(input())
for tc in range(1, 1 + T):
    a = list(map(int, input()))
    N = len(a)
    b = [0] * N
    cnt = 0
    for i in range(N): #비교위치
        if a[i] != b[i]:
            cnt += 1
            for j in range(i, N): # 다른 위치부터 오른쪽 끝까지
                b[j] = a[i]
    print(f'#{tc} {cnt}')
                        