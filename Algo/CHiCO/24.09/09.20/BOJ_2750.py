import heapq
N = int(input())
arr = []
for _ in range(N):
    heapq.heappush(arr, int(input()))

for _ in range(N):
    print(heapq.heappop(arr))