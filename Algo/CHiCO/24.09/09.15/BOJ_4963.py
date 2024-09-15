import sys
input = sys.stdin.readline

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    direction = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
    arr = []
    visited = [[0]*w for _ in range(h)]
    for _ in range(h):
        arr.append(list(map(int, input().split())))
    
    stack = []
    cnt = 0
    for i in range(w):
        for j in range(h):
            if visited[j][i] == 0:
                if arr[j][i] == 1:
                    stack.append((j,i))
                    visited[j][i] = 1
                    while stack:
                        dy,dx = stack.pop()
                        for l in range(8):
                            ny, nx = dy+direction[l][0] , dx+direction[l][1]
                            if 0 <= ny < h and 0 <= nx < w:
                                if arr[ny][nx] == 1 and not visited[ny][nx]:
                                    stack.append((ny,nx))
                                    visited[ny][nx] = 1
                    cnt += 1
    print(cnt)