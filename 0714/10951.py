inputs = []
while True:
    # try:
        # 한 줄씩 입력을 받아서 리스트에 추가합니다.
    line = input()
    print(line,"여기 인풋")
    inputs.append(line)
        # ["1 1","2 3","3 4"]
    # except EOFError:
    #     # EOFError가 발생하면 입력이 끝났다는 의미입니다.
    #     break

# # 입력받은 테스트 케이스에 대해 반복합니다.
# # inputs 안에는 # ["1 1","2 3","3 4"] 가 들어있다
# for line in inputs:
#     # line = "1 1" 그 다음은 line = "2 3"
#     # 입력된 한 줄을 공백을 기준으로 나누어 A와 B로 분리합니다.
#     A, B = map(int, line.split())

#     # A와 B의 합을 출력합니다.
#     print(A + B)