import sys
input = sys.stdin.readline

N, M = map(int, input().split())

hear = set()
for _ in range(N):
    hear.add(input().rstrip())

see = []
for _ in range(M):
    a = input().rstrip()
    if a in hear:
        see.append(a)

see.sort()
print(see)
print(len(see))
for ans in see:
    print(ans)
