# user_board = [list(map(int, input().split())) for _ in range(5)]
# mc_board = [list(map(int, input().split())) for _ in range(5)]

user_board = [int(num) for _ in range(5) for num in input().split()]
mc_board = [int(num) for _ in range(5) for num in input().split()]

print(user_board)

count = 0
# 가/세/대각 체크리스트
x_lst = [0] * 10
y_lst = [0] * 10
di_lst1 = [0] * 10
di_lst2 = [0] * 10

for n in mc_board:
    # mc가 부른 숫자들 순서대로 인덱스 찾기
    a = user_board.index(n)
    # 인덱스로 해당 숫자 위치 계산하기
    x,  y = a//5, a%5
    # 가로,세로,대각선 빙고 카운트 증가
    x_lst[x] += 1
    y_lst[y] += 1
    di_lst1[x+y] += 1
    di_lst2[y-x+4] += 1

    # print(x_lst)
    # print(y_lst)
    # print(di_lst1)
    # print(di_lst2)

    # 빙고 개수 확인해서 count 증가
    if x_lst[x] == 5:
        count += 1
    if y_lst[y] == 5:
        count += 1
    if di_lst1[x+y] == 5 or di_lst2[y-x+4] == 5:
        count += 1
# count 3 되면 종료
    if count == 3:
        print(n)
        break