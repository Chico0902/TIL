n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum = 0
for i in range(m):  # 처음 m개의 구간의 합 구하기
    sum += arr[i]
    max_v = sum
for i in range(n - m):
    sum += arr[i + m]
    sum -= arr[i]
    if sum > max_v:
        max_v = sum
print(max_v)