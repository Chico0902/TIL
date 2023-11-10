T = int(input())
for tc in range(1, T+1):
    forth = list(input().split())
    stack = []
    error = False
    for i in range(len(forth) - 1):
        if forth[i].isdigit(): # 숫자일 경우
            stack.append(forth[i]) # 스택의 증가
        else: # 연산자일 경우 -> 연산 결과를 스택에 추가
            try:
                b = int(stack.pop()) #두 번째 숫자
                a = int(stack.pop()) # 첫 번째 숫자
                if forth[i] == '+':
                    ans = a + b
                elif forth[i] == '-':
                    ans = a-b
                elif forth[i] == '*':
                    ans = a * b
                elif forth[i] == '//':
                    ans = a//b
                stack.append(ans)
            except : # 두개의 숫자를 꺼낼 수 없는 경우
                error = True
        if error == True or len(stack) != 1: #에러 발생 or 스택에 여러 값이 남아있는 경우
            print(f'#{tc} error')
        else:
            print(f'#{tc}. {stack.pop()}')