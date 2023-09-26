from collections import deque
T = int(input())
cnt = 0 # 몇개인지 세는거
for tc in range(T):
    flag = 0 # 나갈지 말지 정하는거
    arr = list(input())
    arr = deque(arr)
    check = [] # 왼쪽부터 뽑아서 여기다가 넣음

    while arr: # arr 전부 뽑을거임
        now = arr.popleft()
        if now in check: #만약 뽑은게 체크리스트에 있으면
            if now != before: #있으면서 before(바로전에 뽑은거)랑 다르면
                flag = 1 # 넌 나가라
                break # 안돌릴거임
            else: #없으면
                continue # 계속 돌려
        else: # 체크리스트에 없으면
            check.append(now) #체크리스트에 넣어
        before = now # 바로전거 갱신해주는거
    if not flag: # 나가지도 않고 다 뽑았으면
        cnt += 1 # 갯수 세줌
print(cnt)
