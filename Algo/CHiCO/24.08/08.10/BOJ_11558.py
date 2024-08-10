T = int(input())
for _ in range(T):
    N = int(input())
    arr = {}
    for i in range(1,N+1):
        arr[i]=int(input())

    start = 1
    cnt = 0
    visited = [0] * (N + 1)

    while start != N:
        if visited[start]:
            cnt = 0
            break
        visited[start] = 1
        cnt += 1
        start = arr[start]
        
    print(cnt)