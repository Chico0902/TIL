N, K = map(int, input().split())
arr = list(range(1,N+1))
ans_list = []
idx = 0
for i in range(1,N+1):
    idx += K-1
    len_arr = len(arr)
    if idx >= len_arr:
        idx = idx % len_arr
    ans_list.append(arr.pop(idx))

print("<" + ", ".join(map(str, ans_list)) + ">")