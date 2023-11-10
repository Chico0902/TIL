T = int(input())

for tc in range(1, 1+T):
    arr = input()
    for i in range(1, 11):
        if arr[:i] == arr[i:2*i]:
            ans = i
            break
    print(f'#{tc} {ans}')