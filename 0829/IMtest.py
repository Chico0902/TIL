T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    ans = list(map(int, input().split()))
    stu_ans = [list(map(int, input().split())) for _ in range(N)]
    m_list = []
    for i in range(N):
        cnt = 0
        plus = 0
        max_val = []
        for j in range(M):
            if stu_ans[i][j] == ans[j]:
                cnt += 1
                cnt = cnt + plus
                plus += 1
                max_val.append(cnt)
            if stu_ans[i][j] != ans[j]:
                plus = 0
        m_list.append(max(max_val))
    print(f'#{tc} {max(m_list)-min(m_list)}')