def sudoku(arr):
    for i in range(9):
        cnt = [0]*10
        for j in range(9):
            cnt[arr[i][j]] += 1
        for k in range(1, 10):
            if cnt[k] == 0: # 1~9에 빠진 숫자가 있으면
                return 0 # 0 리턴


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    ans = sudoku(arr)
    print(f'#{tc} {ans}')
