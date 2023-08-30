for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    v = [0] * (N * N +1) # 연속된 숫자의 유무를 체크하는 리스트
    for i in range(N):
        for j in range(N):
            for r, c in [(0, 1), (1,0), (-1,0), (0,-1)]:
                #격자 내에 있어야 하고, 현재 칸의 숫자 +1이 다음 칸의 숫자인 경우
                if 0 <= i+r < N and 0 <= j+c < N and arr[i][j] + 1 == arr[i+r][j+c]:
                    v[arr[i][j]] = 1 #연속된 숫자임을 표시
    start, cnt, temp = 0, 1, 1
    for i in range(len(v) -1, -1, -1):
        if v[i] == 1: #연속된 숫자의 경우
            temp += 1 #연속 카운트 증가
        else: #연속이 끊긴 경우
            if cnt <= temp: #최댓값 경신
                cnt = temp
                start = i + 1 # 시작점 갱신
            temp = 1 #연속 카운트 초기화
    print(f'#{tc} {start} {cnt}')