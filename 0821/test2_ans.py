T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(input().split())
    B = [] #홀수 카드 저장 Queue
    C = [] # 짝수 카드 저장 Stack
    bonus = 0
    for i in range(N):
        if A[i] == '+': # 더하기 카드의 경우 보너스 숫자 증가
            bonus += 1
        else:
            num = int(A[i]) +bonus #현재 카드와 보너스 숫자를 더한다
            if num % 2 == 1: #결과가 홀수인 경우
                B.append(num) #B덱에 카드 추가
            else:
                C.append(num) #짝수인 경우 C덱에 카드 추가

    for i in range(K): #김싸피의 차례까지 카드를 가져간다
        card1 = B.pop(0) if B else 0
        card2 = C.pop() if C else 0
    print(f'#{tc} {card1 + card2}')