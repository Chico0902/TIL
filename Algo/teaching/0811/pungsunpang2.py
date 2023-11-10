from pprint import pprint

def pang(N,M):
    dy = [0, -1, 0, 1, 0]
    dx = [0, 0, 1, 0, -1]
    cnt_list = []
    for i in range(N):
        for j in range(M):
            hap_list = []
            for k in range(5):
                if 0 <= i+dy[k] <= N-1 and 0 <= j+dx[k] <= M-1:
                    hap_list.append(arr[i+dy[k]][j+dx[k]])
            cnt = sum(hap_list)
            cnt_list.append(cnt)
            ans = max(cnt_list)
    print(f'#{tc} {ans}')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    pang(N, M)









