from pprint import pprint
# N, M = map(int, input().split())
#
# arr = [list(input())for _ in range(N)]
# arr1 = [list(i) for i in zip(*arr)]
# pprint(arr)
# pprint(arr1)
# cnt1 = 0
# cnt2 = 0
# for i in range(N):
#     if 'X' not in arr[i]:
#         cnt1 += 1
# for i in range(M):
#     if 'X' not in arr1[i]:
#         cnt2 += 1
# if cnt1 >= cnt2:
#     print(cnt1)
# else:
#     print(cnt2)
arr = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
arr1 = [list(i) for i in zip(*arr)]
pprint(arr)
pprint(arr1)