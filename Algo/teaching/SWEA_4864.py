#간단방법
T = int(input())
for tc in range(1, 1+T):
    str1 = input()
    str2 = input()
    cnt = 0
    if str1 in str2:
        cnt += 1
    print(f'#{tc} {cnt}')

# --------------------------------------------------
#복잡방법
T = int(input())
for tc in range(1, 1+T):
    str1 = input()
    str2 = input()
    result = 0
    #두번째 문자열 안에서 첫번째 문자열을 찾는다
    for i  in range(len(str2) - len(str1)+ 1 ):
        cnt = 0
        #첫번째 문자열 모든 문자 검사
        for j in range(len(str1)):
            #첫번째 문자열의 j번째와 두번째 문자열의 i+j 가 일치하는 지 확인
            if str1[j] == str2[i+j]:
                cnt += 1
        #카운트가 첫번째 문자열의 길이와 같다면
        if cnt == len(str1):
            result =1
    print(f'#{tc} {result}')