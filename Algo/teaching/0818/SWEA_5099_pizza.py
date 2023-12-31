T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    chz = list(map(int, input().split())) #각 피자의 초기 치즈의 양
    # 피자 인덱스(피자번호), 치즈의 양 을 저장할 리스트
    pizzas = [[i+1, p] for i, p in enumerate(chz)]
    oven = pizzas[:N] #화덕에 처음 넣는 피자들
    remain = pizzas[N:] #화덕에 넣지않은 나머지 피자들

    while len(oven) > 1: #홛거의 피자가 한개 남을때까지 반복
        now = oven.pop(0) #화덕에서 피자 꺼내기
        #now[0] : 현재 피자의 인덱스(번호), now[1] : 현재 피자의 치즈 양
        now[1] //= 2 #치즈의 양을 반으로 줄이기
        if now[1] == 0: #치즈가 모두 녹았다면
            if remain: #남은 피자를 화덕에 넣기
                oven.append(remain.pop(0))
        else: #치즈가 다 안녹았다면, 다시 화더에 넣기
            oven.append(now)
    print(f'#{tc} {oven[0][0]}')