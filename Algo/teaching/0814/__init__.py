jinwoo = input()
taegyu = len(jinwoo)
node = [list(map(int, input().split())) for _ in range(taegyu)]
visited = [0] * taegyu
def DFS(now):

    visited[now] = 1
    print(jinwoo[now], end='')
    for i in range(taegyu):
        if node[now][i] == 1:
            if visited[i] == 0:
                DFS(i)

DFS(0)