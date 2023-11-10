'''
T = int(input())
for tc in range(1, 1+T):
    str1 = input()
    str2 = input()
    cnt_list = []
    #str1 의 문자를 하니씩 st2와 비교
    for i in str1:
        cnt_list.append(str2.count(i))
    result = max(cnt_list)
    print(f'#{tc} {result}')
'''
T = int(input())
for tc in range(1, 1+T):
    str1 = input()
    str2 = input()
    rseult = 0
    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
            if result < cnt:
                result = cnt
    print(f'#{tc} {result}')
