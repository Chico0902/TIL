T = int(input())
for tc in range(1, 1+T):
    all = input()
    N = len(all)
    stack = []
    cnt = 0
    before = '('
    for i in range(N):
        if all[i] == '(':
            stack.append('(')
            before = '('
        elif all[i] == ')':
            if before == '(':
                stack.pop()
                cnt += len(stack)
                before = ')'
            else:
                stack.pop()
                cnt += 1
                before = ')'
    print(f'#{tc} {cnt}')