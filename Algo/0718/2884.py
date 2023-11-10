a, b = map(int, input().split())

H = a*60
M = b
time = H+M
alam = time - 45

new_H = alam//60
new_M = alam%60
if new_H > -1:
    print(new_H,new_M)
elif new_H == -1:
    print(23,new_M)
