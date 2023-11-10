# def sip():
#     global compare1
#     dy = [-1, 0, 1, 0]
#     dx = [0, 1, 0, -1]
#
#     for i in range(N):
#         for j in range(N):
#             fly_out = [arr[i][j]]
#             for k in range(4):
#                 for p in range(1, M):
#                     y = i + dy[k]*p
#                     x = j + dx[k]*p
#                     if 0 <= y < N and 0 <= x < N:
#                         fly_out.append(arr[y][x])
#             if sum(fly_out) > compare1:
#                 compare1 = sum(fly_out)
#
#
# def dae():
#     global  compare1
#     dy = [-1, 1, 1, -1]
#     dx = [1, 1, -1, -1]
#
#     for i in range(N):
#         for j in range(N):
#             fly_out2 = [arr[i][j]]
#             for k in range(4):
#                 for p in range(1, M):
#                     y = i + dy[k] * p
#                     x = j + dx[k] * p
#                     if 0 <= y < N and 0 <= x < N:
#                         fly_out2.append(arr[y][x])
#             if sum(fly_out2) > compare1:
#                 compare1 = sum(fly_out2)
#
# T = int(input())
#
#
# for tc in range(1, T + 1):
#     compare1 = 0
#
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     sip()
#     dae()
#     result = compare1
#     # if compare1 >= compare2 :
#     #     result = compare1
#     # else:
#     #     result = compare2
#     print(f'#{tc} {result}')

def sip():
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    a = 0
    for i in range(N):
        for j in range(N):
            fly_out = arr[i][j]
            for k in range(4):
                for p in range(1, M):
                    y = i + dy[k]*p
                    x = j + dx[k]*p
                    if 0 <= y < N and 0 <= x < N:
                        fly_out += (arr[y][x])
            if fly_out > a:
                a = fly_out
    return a


def dae():
    dy = [-1, 1, 1, -1]
    dx = [1, 1, -1, -1]
    b = 0
    for i in range(N):
        for j in range(N):
            fly_out = arr[i][j]
            for k in range(4):
                for p in range(1, M):
                    y = i + dy[k] * p
                    x = j + dx[k] * p
                    if 0 <= y < N and 0 <= x < N:
                        fly_out += (arr[y][x])
            if fly_out > b:
                b = fly_out
    return b

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = [sip(), dae()]
    print(f'#{tc} {max(ans)}')
