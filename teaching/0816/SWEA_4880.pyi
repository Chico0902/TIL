def win(x ,y):
    if arr[x] == arr[y]: #비긴경우
        return x
    #1 : 가위, 2:바위, 3:보
    elif arr[x] - arr[y] == 1 or arr[x] - arr[y] == -2: # x가 이긴경우
        return x
    return y

def group(start, end):
    if start == end:
        return start # 한명만 남았을때 그 사람의 번호 리턴
    left = group(start, (start +end) // 2) #시작부터 중간까지
    right = group((start + end)//2 + 1, end) #중간 다음부터 끝까지
    return win(left, right)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = group(0, N - 1) + 1
    # N-1 -> 인덱싱, +1 -> 학생번호
    print(f'#{tc} {result}')