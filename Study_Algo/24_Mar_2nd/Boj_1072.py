import math
X,Y = map(int,input().split())
Z = math.floor((Y*100/X))
print(Z)


if X == Y:
    print(-1)
elif Z == 99:
    print(-1)
else:
    start = 0
    end = X
    while start <= end:
        mid = (start + end) // 2
        # print("check",start,end,math.floor((Y+mid/X+mid)*100))
        if math.floor(((Y+mid)/(X+mid))*100) <= Z:
            start = mid + 1
        else:
            end = mid -1
    print(start)

# 이건 왜안됨????????

# import math
# X,Y = map(int,input().split())
# Z = math.floor((Y/X)*100)


# if X == Y:
#     print(-1)
# else:
#     start = 0
#     end = X
#     while start <= end:
#         mid = (start + end) // 2
#         # print("check",start,end,math.floor((Y+mid/X+mid)*100))
#         if math.floor(((Y+mid)/(X+mid))*100) <= Z:
#             start = mid + 1
#         else:
#             end = mid -1
#     print(start)
