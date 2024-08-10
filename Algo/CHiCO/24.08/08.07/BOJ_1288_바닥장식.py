def count_wooden_boards(N, M, floor):
    board_count = 0
    
    for i in range(N):
        for j in range(M):
            # Check horizontal board (row-wise)
            if floor[i][j] == '-':
                board_count += 1
                k = j
                while k < M and floor[i][k] == '-':
                    floor[i][k] = '.'  # Mark as visited
                    k += 1
            
            # Check vertical board (column-wise)
            if floor[i][j] == '|':
                board_count += 1
                k = i
                while k < N and floor[k][j] == '|':
                    floor[k][j] = '.'  # Mark as visited
                    k += 1

    return board_count

# Input reading
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
floor = []
index = 2
for _ in range(N):
    floor.append(list(data[index]))
    index += 1

# Counting the wooden boards
result = count_wooden_boards(N, M, floor)
print(result)
