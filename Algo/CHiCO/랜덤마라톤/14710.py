h, m = map(int, input().split())

new_h = h % 30
if m == new_h*12:
    print('O')
else:
    print('X')