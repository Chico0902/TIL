T = int(input())

for tc in range(1, T + 1):
    cnt = 0 #수정횟수
    now = '0' #현재 비트 값과 비교할 문자열 초기화
    num = input()
    for i in range(len(num)):
        if num[i] != now: #현재 비트값과 now 값이 다르면 -> 수정이 필요
            cnt += 1
            now = num[i] #now값을 현재 비트 값으로 갱신
    print(f'#{tc} {cnt}')
