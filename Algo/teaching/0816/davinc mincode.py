N, M = map(int, input().split())
lst = list(map(int, input().split()))
path = [] #선택된 패들의 값을 저장할 리스트
used = [0] * N # 패가 사용되었는지 체크
Min = 21e8
result = []

def DFS(level, Sum):
    global Min, path, result
    if level == M: #패를 모두 선택 했다면
        if Sum < Min: #현재 곱한 값이 최소값 보다 작으면 최소값 업데이트
            Min = Sum
            result = copy.deepcopy(path) #선택된 패들의 값을 최종 result에 저장
        return

    for i in range(N):
        if used[i] == 1: #이미 사용된 패라면 건너뜀
            continue
        path.append(lst[i]) #패를 선택하고 path에 추가
        used[i] = 1
        DFS(level + 1 , Sum * lst[i])#다음 패를 선택으로 넘억며 재귀호출
        used[i] = 0 #복구(백트래킹)
        path.pop()
DFS(0, 1) #초기레벨은 0, 초기곱은 1
result.sort()
print(*result)