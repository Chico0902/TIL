L = int(input())
arr = list(input())
new_arr = []
for i in arr:
    new_arr.append(ord(i)-96)
ans = 0
for i in range(L):
    ans += new_arr[i]*(31**i)

print(ans%1234567891)