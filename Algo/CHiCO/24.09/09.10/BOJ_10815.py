import sys
input = sys.stdin.readline

N = int(input())
card = set(map(int,input().split()))
M = int(input())
comp = list(map(int, input().split()))
ans = []
for i in comp:
    if i in card:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)