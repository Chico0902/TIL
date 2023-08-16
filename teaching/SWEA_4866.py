T = int(input())
for tc in range(1, T+1):
    text = input()
    stack = [] # 빈 스택 초기화
    for i in text:
        #여는괄호면 스택에 추가 -> append
        if i == '{' or i == "(":
            stack.append(i)
        #닫는 괄호가 중괄호면 짝이 맞는지 확인 후 제거 -> pop
        elif stack and i == "}" and stack[-1] =="{":
            stack.pop()
        #닫는 괄호가 소괄호면 짝이 맞는지 확인 후 제거 -> pop
        elif stack and i == ")" and stack[-1] == "(":
            stack.pop()
        #닫는 괄호인데 짝이 맞지 않아 -> 스택에 추가
        elif i == '}' or i == ')':
            stack.append(i)

    #스택 판별
    #짝이 맞지 않는 경우
    if stack:
        result = 0
    #짝이 맞는 경우
    else:
        result = 1
    print(f'#{tc} {result}')