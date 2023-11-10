# N = int(input())
a = 100
b = 60
while True:    
    c = a - b
    if c <= 0:
        break
    elif c > 0:
        a = b
        b = c
    print(a, b)
# while soo() > 0:
# print(soo)