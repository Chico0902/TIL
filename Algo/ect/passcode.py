# 시도
# T = int(input())
#
# N, K = map(int, input().split())
#
# Sam = list(map(int, input().split()))
# code = list(map(int, input().split()))
#
# for i in range(N):
#     for j in range(K):
#         if Sam[i] == code[j]:
#             Sam = Sam[i:]
#             del code[j]
# if code == []:
#     print(1)
# else:
#     print(0)

#정답 1
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    Sample = list(map(int, input().split()))
    Passcode = list(map(int, input().split()))

    cnt = 0
    result = 0
    for i in range(N):
        if passcode[cnt] == sample([]):
            cnt += 1
        if cnt == K:
            result = 1
            break
    print(f'#{tc} {result}')

#정답 2
    T = int(input())
    for tc in range(1, T + 1):
        N, K = map(int, input().split())
        sample = list(map(int, input().split()))
        passcode = list(map(int, input().split()))

        indexes =[]
        result = 1

        for i in range(len(passcode)):
            now = passcode[i]
            try:
                index = sample.index(now)
                sample = sample[index + 1 :]
            except:
                result = 0
        print(f'#{tc} {result}')