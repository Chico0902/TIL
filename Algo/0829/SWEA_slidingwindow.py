# SWEA 슬라이딩 윈도우
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    # 시작점, 끝점 초기화
    start = 0
    end = m - 1
    # 공통 구간의 초기 합
    midsum = sum(arr[:end])
    # 변수 초기화
    ans = -999999
    s_index = 0
    end_index = 0
    while end < n:
        midsum += arr[end]  # 마지막값 추가
        # 최대값 갱신
        if midsum > ans:
            ans = midsum
            s_index = start
            e_index = end
        midsum -= arr[start]    # 첫번째 값 차감
        start += 1      # 반복문이 진행되는 동안 시작점과 끝점을 하나씩 이동
        end += 1
    print(f'#{tc} {s_index} {e_index} {ans}')