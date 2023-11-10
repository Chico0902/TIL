T = int(input())

def DFS(start, end):
    stack = []
    visited = [0] * (V+1)
    stack.append(start)
    while stack:
        now = stack.pop()
        stack.append()




for tc in range(1, T+1):
    V, E = map(int, input().split())

    arr = [[0] * (V + 1) for _ in range(V + 1)]

# 노드와 간선 갯수 받고 노드 수 만큼 인접행렬 초기화 하고
# for 반복문 써서 노드 값 받아서 인접행렬에 값 넣고