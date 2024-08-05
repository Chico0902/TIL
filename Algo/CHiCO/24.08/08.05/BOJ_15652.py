import sys
input = sys.stdin.read

# 입력 처리
data = input().strip().split()
N = int(data[0])
M = int(data[1])

# 현재 수열을 저장할 리스트
current_sequence = []

def backtrack(start):
    if len(current_sequence) == M:
        print(' '.join(map(str, current_sequence)))
        return
    
    for i in range(start, N + 1):
        current_sequence.append(i)
        backtrack(i)
        current_sequence.pop()

# 백트래킹 시작
backtrack(1)
