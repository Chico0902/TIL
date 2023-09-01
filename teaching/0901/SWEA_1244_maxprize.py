from collections import deque
T = int(input())

arr, change = map(int, input().split())

arr = sorted(arr)
d_arr = deque(arr)
while len(arr) > 2:
    if arr[-1] == max(arr):
        arr.pop()