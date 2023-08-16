# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# dit = {}
#
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == 1:
#             dit[i] = j
#
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def DFS(now):
    #현재 방문한 노드 출력
    print(now, end =' ')
    for i in range(N):
        #현재 노드와(now) i 번째 노드가 연결되어 있다면
        if arr[now][i] == 1:
            #재귀적으로 i번째 노드 방문
            DFS(i)
# 첫번째 노드부터 탐색 시작
DFS(0)