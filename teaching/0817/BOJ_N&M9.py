from itertools import permutations
N, M = map(int, input().split())
arr = list(map(int, input().split()))

a = list(set(permutations(arr, M)))
b = sorted(a)
for i in range(len(a)):
    print(*b[i])

