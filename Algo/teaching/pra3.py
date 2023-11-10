Y, M, D = input().split('.')

cnt = 0
ans = 0
if M == 'X':
    cnt += 9
    if D == 'X':
        cnt *= 9
    elif D == '1X':
        cnt *= 10
    elif D == '2X':
        cnt *= 10
    elif D == '3X':
        cnt *= 2
    elif D == 'XX':
        cnt *= 22

elif M == 'XX':
    cnt += 3
    if D == 'X':
        cnt *= 9
    elif D == '1X':
        cnt *= 10
    elif D == '2X':
        cnt *= 10
    elif D == '3X':
        cnt *= 2
    elif D == 'XX':
        cnt *= 22
else:
    cnt = 1

print(cnt)

