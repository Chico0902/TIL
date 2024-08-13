# 문제를 잘 읽읍시다...

# N = int(input())
# arr = list(input())

# max_cnt = 0
# min_cnt = 0
# cnt = 0
# for i in arr:
#     if i == 'E':
#         cnt += 1
#         if max_cnt < cnt:
#             max_cnt = cnt
#     else:
#         cnt -= 1
#         if min_cnt > cnt:
#             min_cnt = cnt
# max_len = abs(max_cnt) + abs(min_cnt) + 1
# if N % max_len == 0:
#     ans = N // max_len
# else:
#     na = N % max_len
#     if max_cnt > abs(min_cnt):
#         if na > max_cnt:
#             ans = (N // max_len) + 1
#         else:
#             ans = N // max_len
#     else:
#         if na > abs(min_cnt):
#             ans = (N // max_len) + 1
#         else:
#             ans = N // max_len
# print(ans)

N = int(input())
arr = list(input())
cnt = 0
for i in range(N):
    if arr[i] == 'W' and arr[i-1] == 'E':
        cnt += 1 
print(cnt)