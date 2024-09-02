import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))
ans = []

while q:
    idx, paper = q.popleft()
    ans.append(idx + 1)

    if paper > 0:
        q.rotate(-(paper - 1))
    elif paper < 0:
        q.rotate(-paper)

print(' '.join(map(str, ans)))



# 더 좋은 방법

import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))

# 풍선을 (번호, 적힌 수) 형태로 리스트에 저장
balloons = [(i + 1, numbers[i]) for i in range(N)]
result = []  # 터진 풍선의 순서를 기록
index = 0  # 시작 인덱스

# 풍선이 다 터질 때까지 반복
while balloons:
    # 현재 인덱스의 풍선을 터뜨리고 제거
    balloon_num, move = balloons.pop(index)
    result.append(balloon_num)  # 터진 풍선의 번호를 결과에 추가

    if not balloons:  # 모든 풍선이 터진 경우 반복 종료
        break

    # 이동할 위치 계산
    if move > 0:
        index = (index + (move - 1)) % len(balloons)  # 오른쪽으로 이동
    else:
        index = (index + move) % len(balloons)  # 왼쪽으로 이동

# 결과 출력
print(' '.join(map(str, result)))
