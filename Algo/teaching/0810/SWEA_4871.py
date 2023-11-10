T = int(input())

def DFS(start, end):
    stack = [] #탐색할 노드를 저장할 스택 초기화
    visited = [False] * (V+1)
    stack.append(start) #시작점을 스택에 넣음
    while stack: # 스택이 비어있으면 반복문 종료
        now = stack.pop()# 스택의 마지막 노드를 꺼냄
        visited[now] = True #현재 노드를 방문
        for next in range(1, V + 1):
            if node[now][next] and not visited[next]: #방문하지 않았고, 연결되어 있다면
                stack.append(next)#스택에 추가
    if visited[end]: #끝점에 방문했다면
        return 1
    else:
        return 0

for tc in range(1, T+1):
    V, E = map(int, input().split()) #노드와, 간선의 개수
    node = [[0 for _ in range(V+1)] for _ in range(V+1)] #인접행렬 초기화
    for _ in range(E):
        start, end = map(int, input().split())
        node[start][end] = 1 # 해당 인접행렬에 1 할당 -> 연결됨
    S, G = map(int, input().split())
    print(f'#{tc} {DFS(S, G)}')