# T = int(input())
#
# for tc in range(1, 1+T):
#     N = int(input())
#     sincung = {}
#     for _ in range(N):
#         start, end = map(int, input().split())
#         sincung[start] = end
#     sincung = sorted(sincung.items(), key=lambda x:x[1])
#     print(sincung)


# SWEA 5202 화물 도크
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 작업 시작 시간, 종료시간 입력
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 오름차순 -> 종료시간이 빠른 작업부터 처리
    arr.sort(key=lambda x : x[1])
    end, cnt = 0, 0     # 마지막 작업이 끝난 시각, 화물차의 수 초기화
    for s, e in arr:
        if s >= end:    # 작업수행 -> 현재 작업의 시작 시간이 마지막 작업의 종료시간보다 크면
            end = e     # 1. 종료시간 업데이트
            cnt += 1    # 2. 작업을 수행한 화물차 수 1 증가
    print(f'#{tc} {cnt}')


