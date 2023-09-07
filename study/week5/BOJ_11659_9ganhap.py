# # 시간 초과
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# for _ in range(M):
#     A, B = map(int, input().split())
#     print(sum(arr[A-1:B]))

import sys
input = sys.stdin.readline
#누적합?
def prefix_sum(N):
    prefixsum = [0] * (N+1)
    prefixsum[0] = 0
    for i in range(1, N+1):
        prefixsum[i] = prefixsum[i-1] + arr[i-1]
    return prefixsum

N, M = map(int, input().split())
arr = list(map(int, input().split()))
c = prefix_sum(N)
print(c)
for _ in range(M):
    a,b = map(int, input().split())
    print(c[b]-c[a-1])

# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# S = prefix_sum(N)
# for _ in range(M):
#     A, B = map(int, input().split())
#     partsum = prefixsum[B] - prefixsum[i-1]