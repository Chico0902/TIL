# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# stk = [0]
# def DFS(a):
#
#     for i in range(N):
#         if arr[a][i] == 1:
#             stk.append(i)
#             DFS(a)

#-----------------------------------------------------

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * 3 #현재 경로에서 방문한 노드를 저장할 리스트

def DFS(now, level):
    global visited
    visited[level] = str(now) #현재 방문한 노드를 저장
    if level == 2: # 모든 노드를 방문했으면 -> 노드를 출력
        print(' '.join(visited))
    for i in range(N):
        if arr[now][i] == 1: # 연결되어 있다면
            DFS(i, level +1)
DFS(0, 0)