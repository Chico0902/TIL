N = int(input())

com = set()
for _ in range(N):
    name,log = input().split()
    if log == 'enter':
        com.add(name)
    else:
        com.remove(name)

comp = list(com)
comp.sort()
for i in range(len(comp)):
    ans = comp.pop()
    print(ans)
