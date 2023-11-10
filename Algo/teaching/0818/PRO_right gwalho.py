def solution(s):
    stack = []
    if s[0] == ')':
        return False
    elif s[0] == '(':
        stack.append(s[0])
    for i in range(1, len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            if stack == []:
                return False
            else:
                stack.pop()
    if stack == []:
        return True
    else :
        return False