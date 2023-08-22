def ga():
    global flag
    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(5):
                if (j+k) < N:
                    if pan[i][j+k] == 'o':
                        cnt += 1
                    if cnt == 5:
                        flag = 1


def se():
    global flag
    for j in range(N):
        for i in range(N):
            cnt = 0
            for k in range(5):
                if (i + k) < N:
                    if pan[i+k][j] == 'o':
                        cnt += 1
                if cnt == 5:
                    flag = 1


def dae1():
    global flag
    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(5):
                if 0 <= (i+k) < N and 0 <= (j+k) < N:
                    if pan[i+k][j+k] == 'o':
                        cnt += 1
            if cnt == 5:
                flag = 1


def dae2():
    global flag
    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(5):
                if 0 <= (i + k) < N and 0 <= (j - k) < N:
                    if pan[i + k][j - k] == 'o':
                        cnt += 1
            if cnt == 5:
                flag = 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pan = [list(input())for _ in range(N)]
    flag = 0
    ga()
    se()
    dae1()
    dae2()
    if flag == 1:
        print(f'#{tc} {"YES"}')
    else:
        print(f'#{tc} {"NO"}')
