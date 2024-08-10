import sys
input = sys.stdin.readline

M = int(input())
arr = set()

for _ in range(M):
    r = input().split()
    
    if len(r) == 1:
        y = r[0]
    elif len(r) == 2:
        y = r[0]
        num = int(r[1])
        
    if y == 'add':
        arr.add(num)
    elif y == 'remove':
        arr.discard(num)
    elif y == 'check':
        if num in arr:
            print(1)
        else:
            print(0)
    elif y == 'toggle':
        if num in arr:
            arr.remove(num)
        else:
            arr.add(num)
    elif y == 'all':
        arr = set(range(1, 21))
    elif y == 'empty':
        arr.clear()
