import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
sumTree = 0
checkhigh = 0
checkpoint = 0
ans = 0
newsumTree = 0
while sumTree < M:
    for i in range(1,N):
        cutTree = arr[i-1] - arr[i]
        sumTree += cutTree*i
        if sumTree == M:
            ans = arr[i]
            newsumTree = M
            break
        elif sumTree > M:
            checkhigh = arr[i-1]
            checkpoint = i
            newsumTree = sumTree - cutTree*i
            break
    break
print(checkhigh)
print(checkpoint)
print(newsumTree)
while newsumTree < M:
    for i in range(1,M):
        newcut = checkpoint*i
        newsumTree += newcut
        if newsumTree > M:
            ans = checkhigh-(i+1)
            break

print(ans)








