# 문제
# 다섯종류 카드 입력(0~9)
# 다섯종류 숫자카드에서 4장 뽑음
# 뽑을때마다 전에 뽑았떤 카드번호와 간격이 3이하로 차이나는
# 중복순열이 몇가지인지 출력
# 재귀호출 이용
# ex) 카드 종류가 1,2,3,4,5 일때
# 1111 : ok
# 1112 : ok
# 1113 : ok
# 1114 : ok
# 1115 : [NO]
# 1121 : ok
# ...
# no count 숫자 : 1251, 5123.. 등등등

card = list(input())
path = [0] * 4 # 카드를 4장 뽑는다 -> 경로가 4
cnt = 0

def card_cnt(level):
    global cnt
    # 4자의 카드를 뽑았으면 경우의 수 증가
    if level == 4:
        cnt += 1
        return # 재귀 호출 종료

    for i in range(5): # 5개의 카드 중 하나 선택
        path[level] = card[i] # 현재 레벨 경로에 -> 선택한 카드를 저장
        # 연속된 카드 간의 차이가 4 이상이면 -> 다음 카드를 선택 -> 백트래킹
        if int(path[level]) - int(path[level - 1]) >= 4:
            continue
        if int(path[level - 1]) - int(path[level]) >= 4:
            continue
        #다음 레벨로 재귀 호출
        card_cnt(level + 1)
card_cnt(0) # 시작 레벨은  0
print(cnt)