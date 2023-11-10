# SWEA 구간의 합
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 투 포인터 초기화
left, right = 0, 0
sum, cnt = 0, 0

while right <= n:
    # 중간합(sum)이 목표값(m)보다 작을 경우
    if sum < m:
        if right < n:   # 리스트 범위를 넘어가지 않게
            sum += arr[right]
        right += 1
    # 중간합(sum)이 목표값(m)보다 클 경우
    if sum > m:
        sum -= arr[left]
        left += 1
    # 중간합(sum)이 목표값(m)과 같을 경우
    if sum == m:
        cnt += 1
        if right < n:   # 리스트 범위를 넘어가지 않게
            sum+= arr[right]
        right += 1
print(cnt)