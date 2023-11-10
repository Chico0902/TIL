# from collections import deque

# N, M = int(input())
# miro = [list(map(int, input())) for _ in range(N)]
# visited = [[0]* N for _ in range(M)]
# distance = [[0] * N for _ in range(M)]
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0,-1]

# def BFS():
#     q = deque()
#     start = (0, 0)
#     q.append(start)
#     visited[start[0]][start[1]] = 1
#     distance[start[0]][start[1]] = 1
#     while q:
#         now = q.popleft()
#         if now[0] == N-1 and now[1] == M-1:
#             break
#         else:
#             for i in range(4):
#                 if


from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def BSF():
    distance = [([0] * (M + 1)) for _ in range(N + 1)]
    start = [0,0]
    q = deque()
    q.append(start)
    distance[0][0] = 1
    while q:
        now = q.popleft()
        if arr[now[0]][now[1]] == 1:
            for i in range(4):
                next_y = now[0]+dy[i]
                next_x = now[1]+dx[i]
                if 0 <= next_y < N and 0 <= next_x < M:
                    if arr[next_y][next_x] == 1 and distance[next_y][next_x] == 0:
                        q.append([next_y,next_x])
                        distance[next_y][next_x] = distance[now[0]][now[1]] + 1
                if next_y == N-1 and next_x == M-1:
                    return(distance[next_y][next_x])
                    

print(BSF())
