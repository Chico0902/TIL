n = int(input())

Stack = []
ans_list = []
flag = 0
last_stack = 1

for _ in range(n):
    now = int(input())
    while last_stack <= now:
        Stack.append(last_stack)
        ans_list.append('+')
        last_stack += 1

    if Stack[-1] == now:
        Stack.pop()
        ans_list.append('-')
    
    elif Stack[-1] > now:
        flag = 1
        break

if flag == 1:
    print('NO')
else:
    print(*ans_list,sep='\n')
