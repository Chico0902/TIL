n = int(input())
cnt = 0
if n >= 500:
    cnt += n // 500
    n %= 500
if n >= 100:
    cnt += n // 100
    n %= 100

if n >= 50:
    cnt += n // 50
    n %= 50

if n >= 10:
    cnt += n // 10
    n %= 10

print(cnt)