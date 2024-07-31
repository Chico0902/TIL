N, M = map(int, input().split())
arr = list(i for i in range(1,N+1))
for _ in range(M):
    c1, c2 = map(int, input().split())
    change1 = arr[c1-1]  
    change2 = arr[c2-1]
    arr[c1-1] = change2
    arr[c2-1] = change1

print(*arr)