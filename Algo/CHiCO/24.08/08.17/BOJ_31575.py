from collections import deque

def can_reach_exchange(N, M, grid):
    # BFS로 경로 탐색
    queue = deque([(0, 0)])
    visited = [[False] * N for _ in range(M)]
    visited[0][0] = True

    # 방향벡터: 오른쪽(동쪽)과 아래쪽(남쪽)으로만 이동 가능
    directions = [(0, 1), (1, 0)]

    while queue:
        x, y = queue.popleft()

        # 목적지에 도달하면 Yes를 반환
        if x == M - 1 and y == N - 1:
            return "Yes"

        # 다음 이동 가능한 위치를 확인
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

    # 목적지에 도달하지 못하면 No를 반환
    return "No"

# 입력 받기
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]

# 결과 출력
print(can_reach_exchange(N, M, grid))
