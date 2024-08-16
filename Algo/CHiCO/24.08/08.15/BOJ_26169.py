def can_eat_two_apples(board, start_r, start_c):
    # 상하좌우 방향 정의
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 스택에 (현재 행, 현재 열, 이동 횟수, 먹은 사과 수, 보드 상태)를 저장
    stack = [(start_r, start_c, 0, 0, [row[:] for row in board])]
    
    while stack:
        r, c, moves, apples, curr_board = stack.pop()
        
        if moves > 3:  # 이동이 3회를 초과하면 중단
            continue
        
        # 2번째 이동에서 사과를 하나도 못 먹었다면 더 진행할 필요가 없음
        if moves == 2 and apples == 0:
            continue
        
        if apples >= 2:  # 사과를 2개 이상 먹으면 성공
            return True
        
        # 현재 위치를 장애물로 변경
        curr_board[r][c] = -1
        
        # 상하좌우로 이동
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 5 and 0 <= nc < 5 and curr_board[nr][nc] != -1:
                if curr_board[nr][nc] == 1:
                    # 사과를 먹으면 사과 개수 증가
                    stack.append((nr, nc, moves + 1, apples + 1, [row[:] for row in curr_board]))
                else:
                    stack.append((nr, nc, moves + 1, apples, [row[:] for row in curr_board]))
    
    return False

# 보드 입력 받기
board = []
for _ in range(5):
    board.append(list(map(int, input().split())))

# 학생의 초기 위치
r, c = map(int, input().split())

# 스택을 이용해 두 개 이상의 사과를 먹을 수 있는지 탐색
if can_eat_two_apples(board, r, c):
    print(1)
else:
    print(0)
