def DFS(idx, now_sum):
    global min_sum
    if now_sum >= min_sum: # 현재 합이 최소 합보다 크면 더이상 탐색 x
       return
    if idx == N: #모든 행을 선택
       if min_sum > now_sum: #최소값 코드
        min_sum = now_sum
        return
    for i in range(N):
        if not used[i]: # 해당 열이 아직 사용되지 않았다면
            used[i] = 1
            DFS(idx + 1, now_sum + arr[idx][i])# 행을 다음행으로 넘어가면서 재귀호출
            used[i] = 0 # 복구(백트래킹)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    used = [0] * N
    min_sum = 21e8
    DFS(0,0)
    print(f'#{tc} {min_sum}')