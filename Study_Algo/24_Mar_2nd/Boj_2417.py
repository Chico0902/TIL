# import math

# n = int(input())
# ans = math.ceil(math.sqrt(n))


# print(ans)
# 서운하네 정말

# def bin(arr,start,end,n):
#     while start <= end:
#         mid = (start+end)//2

#         if mid**2 > n:
#             end = mid
#         elif mid**2 < n:
#             start = mid
#         else:
#             print(mid)



# n = int(input())

# 답 : 

n = int(input())

start = 0
end = n

while start <= end:
    mid = (start + end) // 2
    if mid ** 2 < n:
        start = mid + 1
    else:
        end = mid - 1

print(start)