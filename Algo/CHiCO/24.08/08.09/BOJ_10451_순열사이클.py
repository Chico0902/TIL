T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    graph = {i+1 : arr[i] for i in range(N)}
    visited = [0] * (N+1)
    cycle = 0
    for i in range(1, N+1):
        if not visited[i]:
            stack = [i]
            while stack:
                now = stack.pop()
                if not visited[now]:
                    visited[now] = 1
                    stack.append(graph[now])
            cycle += 1
    print(cycle)