MJY = list(input())

# 그래프의 기본 구성 요소 : 노드, 간선
# R -> K _> B-> I -> F- > C -> C -> M
# 인접행렬

# 첫번째 노드(0)는 두번째 노드(1), 세번째 노드(2), 서번째 노드(3)와 연결되어있다.
# 두번째 노드(1)는 다섯번째 노드(4), 여섯번째 노드(5) 와 연결되어있다.
# 네번째 노드(3)는 일곱전째 노드(6), 여덟번째 노드(7)와 연결되어있다.

lst = list(input())# 노드를 입력
N = len(lst)# 노드의 개수
adj = [list(map(int, input().split()))for _ in range(N)]# 인접 행렬 입력
visited = [False for _ in range(N)]# 방문 여부를 저장하는 리스트, 처음에는 Fasle 초기화

def DFS(v):
    print(lst[v], end='')# 현재 방문한 노드 출력
    visited[v] = True

    for i in range(N):
        if adj[v][i] and not visited[i]: # 연결되있고,아직 방문하지 않았다면
            DFS(i) #탐색 계속

DFS(0) # 0번 노드부터 시작하여 탐색