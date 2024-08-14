N = int(input())
arr = [0]
for _ in range(N):
    arr.append(int(input()))

stack = []
cnt_list = []
for i in range(1,N+1):
    visited = [0] * (N+1)
    cnt = 0
    stack.append(arr[i])
    visited[i] = 1
    while stack:
        now = stack.pop()
        if visited[now] == 0:
            stack.append(arr[now])
            cnt += 1
            visited[now] = 1
    cnt_list.append(cnt)

print(cnt_list.index(max(cnt_list))+1)