N = int(input())

arr = list(map(int, input().split()))

ans = float("inf")

i=0
j=1

X = 0
Y = 0

while arr[i] != arr[-j]:
    # print(i,j,ans)
    if ans > abs(arr[i]+arr[-j]):
        ans = abs(arr[i]+arr[-j])
        X = i
        Y = -j
        if arr[i]+arr[-j] < 0:
            i += 1
        elif arr[i]+arr[-j] > 0:
            j += 1
        else:
            # print(1)
            break
    else:
        # print(2)
        break

print(arr[X],arr[Y])

