for tc in range(10):
    N = int(input())
    arr = input()
    stack = []
    num_list = []
    for i in range(113):
        if i == '(':
            stack.append(i)
        if i == ')':
            while stack[-1] == '(':
                num_list.append(stack.pop())
        if i == '+':
            stack.a 