import heapq

N,K = map(int, input().split())
bosuk = []


for _ in range(N):
    M,V = map(int, input().split())
    heapq.heappush(bosuk, (M,V))

print(bosuk)

heapq.heapify(bosuk)
print(bosuk)

heapq.heappop(bosuk)

print(bosuk)