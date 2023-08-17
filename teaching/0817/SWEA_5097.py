# 스택 : 후입선출 - 최근에 추가된 데이터가 먼저 삭제
# append, pop
# 데이터 추가 : push, 데이터삭제 : pop
# DPS로 활용

# 큐 : 선입선출 - 먼저 추가된 데이커가 먼저 삭제
# 데이터 추가 : enqueue, 데이터 삭제 : dequeue
# append, pop(0)

# from collections import deque
# # deque 양쪽 끝에서 삽입과 삭제가 이루어짐
# d = deque()
# d.append(1)
# d.extend([10, 15, 20])
# d.popleft()
# d.pop()

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(M):
        arr.append(arr.pop(0))
    result = arr[0]
    print(f'#{tc} {result}')