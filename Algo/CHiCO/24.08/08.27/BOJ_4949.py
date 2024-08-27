while True:
    a = input()
    stack = []
    ans = 'yes'
    if a == '.':
        break
    for i in a:
        if i == '(':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        elif i == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    ans = 'no'
                    break
            else:
                ans = 'no'
                break
        elif i == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    ans = 'no'
                    break
            else:
                ans = 'no'
                break
    if stack:
        ans = 'no'
    print(ans)
