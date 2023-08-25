# n = int(input())
#
# arr = list(map(int, input().split()))
# dp = [float(-'inf')] * (n+1) # 지금까지의 합
#
# jump = [2, 7]
#
# dp = max(dp, dp[i - jump[i]]) # dp와 지금까지의 dp와 현재 좌표의 합, 둘 중 최솟값
n = int(input())
map_info = list(map(int, input().split()))

dp = [float('-inf')] * (n + 1)
dp[0] = 0
for i in range(n + 1):
    if dp[i] == float('-inf'):
        continue

    for jump in [2, 7]:
        next_position = i + jump
        if next_position <= n:
            dp[next_position] = max(dp[next_position], dp[i] + map_info[next_position - 1])

print(max(dp[-7:]))