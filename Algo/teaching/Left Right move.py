arr = ['3', '5', '1', '9', '7']

T = list(input() for _ in range(4))

def Right(lst):
    #리스트 뒤쪽에 앞의 4개의 원소 추가
    for i in range(4):
        lst.append(lst[i])
    #리스트 양쪽의 4개의 원소 제거
    for _ in range(4):
        lst.pop(0)

def left(lst):
    lst.append(lst[0])
    lst.pop(0)

for i in range(4):
    if T[i] == 'R':
        Right(arr)
    if T[i] == 'L':
        left(arr)

print(*arr)