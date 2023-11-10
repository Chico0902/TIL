# from collections import deque
#
# T = int(input())
# q = deque()
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0 ,-1]
#
# def BFS(start):
#     visited = [[0] * 5 for _ in range(5)]
#     q = [start]
#     a = start[0]
#     b = start[1]
#     while q:
#         now = q.pop()
#         for k in range(4):
#             if 0 <= a + dy[k] < N and 0 <= b+dy[k] < N:
#                 if miro[a+dy[k]][b+dx[k]] == 0:
#                     visited[a+dy[k]][b+dx[k]] =
#
# for tc in range(1, 1+T):
#     N = int(input())
#     miro = [list(map(int, input().split())) for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if miro[i][j] == 2:
#                 start = (i, j)


#-----------------------------------------------------------------------------

T = int(input())
# 방향 탐색 선언
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


for tc in range(1, T + 1):
    N = int(input())
    # 행렬 선언
    matrix = [list(map(int, input())) for _ in range(N)]
    # 방문 처리
    visited = [[False] * N for _ in range(N)]
    # 거리 리스트 생성 이거랑 visited 합쳐도 상관없음
    distance = [[0] * N for _ in range(N)]
    # 2인 경우 찾고 난 후 flag 를 통해서 불필요한 연산 없이 반복문 종료
    flag = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                # 시작 위치 설정
                queue = [(i, j)]
                while queue:
                    # queue 0 번인덱스값 추출
                    check = queue.pop(0)
                    # 방향 탐색
                    for k in range(4):
                        x = check[1] + dx[k]
                        y = check[0] + dy[k]
                        # 범위 내에 있는 경우
                        if (0 <= x < N) and (0 <= y < N):
                            # 방문하지 않았고 1이 아닌 경우
                            if not visited[y][x] and matrix[y][x] != 1:
                                # queue에 값 추가
                                queue.append((y, x))
                                # 방문 처리
                                visited[y][x] = True
                                # 조건에 맞는 y,x 에 이전의 distance 값에 + 1 해줌
                                distance[y][x] = distance[y - dy[k]][x - dx[k]] + 1
                                # 탐색을 진행하다 3인 경우
                                if matrix[y][x] == 3:
                                    # distance 값에서 시작 위치로 증가한 1 빼줌
                                    print(f"#{tc} {distance[y][x]-1}")
                                    # flag 변수로 더이상 탐색하지 않도록 1 넣어준 후 break
                                    flag = 1
                                    break
                    # 반복문을 진행하며 flag 값이 1인 경우 탈출
                    if flag == 1:
                        break
                # flag 변수로 반복문을 탈출하지 않을 경우 => 3으로 갈 수 없는 경우라서 0 출력
                else:
                    print(f"#{tc} 0")
            # flag 값으로 탈출 조건 선언
            if flag == 1:
                break
        # flag 값으로 탈출 조건 선언
        if flag == 1:
            break
