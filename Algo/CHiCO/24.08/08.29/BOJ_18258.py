from sys import stdin, stdout
from collections import deque

# 큐 초기화
queue = deque()

# 입력 수 N 받기
N = int(stdin.readline().strip())

# 결과를 저장할 리스트
results = []

# 명령 처리
for _ in range(N):
    command = stdin.readline().strip()
    
    if command.startswith("push"):
        # "push X" 명령 처리
        _, value = command.split()
        queue.append(int(value))
    elif command == "pop":
        # "pop" 명령 처리
        if queue:
            results.append(queue.popleft())
        else:
            results.append(-1)
    elif command == "size":
        # "size" 명령 처리
        results.append(len(queue))
    elif command == "empty":
        # "empty" 명령 처리
        if queue:
            results.append(0)
        else:
            results.append(1)
    elif command == "front":
        # "front" 명령 처리
        if queue:
            results.append(queue[0])
        else:
            results.append(-1)
    elif command == "back":
        # "back" 명령 처리
        if queue:
            results.append(queue[-1])
        else:
            results.append(-1)

# 결과 출력
stdout.write('\n'.join(map(str, results)) + '\n')