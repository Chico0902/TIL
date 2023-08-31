a, b = map(int, input().split())
cnt = 0
while b >= a:
    if b == a:
        print(cnt)
        exit()
    if b % 10 == 1: #1의 자리가 1인 경우, 1을 제거
        b //= 10
    elif b % 2 == 0: #짝수 인 경우 2로 나눈다
        b //= 2
    else: # 이 두 조건에 해당하지 않으면, b를 a로 만들 수 없다
        print(-1)
        exit()
    cnt += 1 #연산을 한번 수행했으므로 cnt 1씩 증가
print(-1) #연산 끝난 후에 b가 a보다 작아질 수 있음.