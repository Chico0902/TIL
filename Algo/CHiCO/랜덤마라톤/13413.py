T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(input())
    goal = list(input())
    btow = 0
    wtob = 0
    for i in range(N):
        if arr[i] == 'W':
            if goal[i] == 'B':
                wtob += 1
        else:
            if goal[i] == 'W':
                btow += 1
        
        if btow >= wtob:
            ans = btow
        else:
            ans = wtob
    print(ans)