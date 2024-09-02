from collections import deque
import sys
input = sys.stdin.read

def main():
    commands = input().splitlines()
    N = int(commands[0])  # 첫 줄에 명령의 수 N
    deque_instance = deque()
    output = []

    for i in range(1, N + 1):
        command = commands[i]
        
        if command[0] == '1':  # 명령어가 '1 X'로 시작하는 경우
            X = int(command.split()[1])
            deque_instance.appendleft(X)
        
        elif command[0] == '2':  # 명령어가 '2 X'로 시작하는 경우
            X = int(command.split()[1])
            deque_instance.append(X)
        
        elif command == '3':
            if deque_instance:
                output.append(deque_instance.popleft())
            else:
                output.append(-1)
        
        elif command == '4':
            if deque_instance:
                output.append(deque_instance.pop())
            else:
                output.append(-1)
        
        elif command == '5':
            output.append(len(deque_instance))
        
        elif command == '6':
            output.append(1 if not deque_instance else 0)
        
        elif command == '7':
            if deque_instance:
                output.append(deque_instance[0])
            else:
                output.append(-1)
        
        elif command == '8':
            if deque_instance:
                output.append(deque_instance[-1])
            else:
                output.append(-1)
    
    # 출력 결과를 한 번에 출력
    sys.stdout.write('\n'.join(map(str, output)) + '\n')

if __name__ == "__main__":
    main()
