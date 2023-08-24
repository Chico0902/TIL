def g_swi():
    if sw

N = int(input())
switch = list(map(int, input().split()))
hak = int(input())
for i in range(hak):
    sex, num = map(int, input().split())
    if sex == 1:
        while num < len(switch):
            if switch[num-1] == 1:
                switch[num-1] = 0
                num *= 2
            elif switch[num-1] == 0:
                switch[num-1] = 1
                num *= 2

    if sex == 2:
        if switch[num - 1] == switch[num + 1]:
            if switch[num-1] == 1:
                switch[num - 1] = 0
                switch[num + 1] = 0
            elif switch[num - 1] == 0:


