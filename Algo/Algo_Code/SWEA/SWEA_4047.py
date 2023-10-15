# T = int(input())
# for tc in range(1, T+1):
#     S = []
#     D = []
#     H = []
#     C = []
#     flag = 0
#     Deck = input()
#     while Deck:
#         now = Deck[1:3]
#         if Deck[0] == 'S':
#             if now in S:
#                 print(f'#{tc}', 'ERROR')
#                 flag = 1
#                 break
#             S.append(now)
#             Deck = Deck[3:]
#         elif Deck[0] == 'D':
#             if now in D:
#                 print(f'#{tc}', 'ERROR')
#                 flag = 1
#                 break
#             D.append(now)
#             Deck = Deck[3:]
#         elif Deck[0] == 'H':
#             if now in H:
#                 print(f'#{tc}', 'ERROR')
#                 flag = 1
#                 break
#             H.append(now)
#             Deck = Deck[3:]
#         elif Deck[0] == 'C':
#             if now in C:
#                 print(f'#{tc}', 'ERROR')
#                 flag = 1
#                 break
#             C.append(now)
#             Deck = Deck[3:]
#         ls = 13-len(S)
#         ld = 13-len(D)
#         lh = 13-len(H)
#         lc = 13-len(C)
#         ans = [ls, ld, lh, lc]
#     if flag == 0:
#         print(f'#{tc}',*ans)
#
T = int(input())
for tc in range(1, T + 1):
    S = list(input())
    card_dict = {"S": [], "D": [], "H": [], "C": []}
    insufficient_card_list = []

    for idx in range(len(S) // 3):
        if int(S[idx * 3 + 1]) * 10 + int(S[idx * 3 + 2]) in card_dict[S[idx * 3]]:
            print(f"#{tc} ERROR")
            break
        else:
            card_dict[S[idx * 3]].append(int(S[idx * 3 + 1]) * 10 + int(S[idx * 3 + 2]))
    else:
        for shape in card_dict:
            insufficient_card_list.append(13 - len(card_dict[shape]))

        print(f"#{tc}", *insufficient_card_list)

        T = int(input())

        for tc in range(1, T + 1):
            cnt = 0  # 수정횟수
            now = '0'  # 현재 비트 값과 비교할 문자열 초기화
            num = input()
            for i in range(len(num)):
                if num[i] != now:  # 현재 비트값과 now 값이 다르면 -> 수정이 필요
                    cnt += 1
                    now = num[i]  # now값을 현재 비트 값으로 갱신
            print(f'#{tc} {cnt}')
