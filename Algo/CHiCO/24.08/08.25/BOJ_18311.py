N ,K = map(int,input().split())
course = list(map(int, input().split()))


half_len = 0
for i in course:
    half_len += i

if K > half_len:
    K = K - half_len
    now = N
    course.reverse()
    while K > 0:
        for i in course:
            K = K - i
            if K >= 0:
                now -= 1
    print(now)
else:
    now = 1
    while K > 0:
        for i in course:
            K = K - i
            if K >= 0:
                now += 1
    print(now)
