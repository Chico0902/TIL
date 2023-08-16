arr = ['3', '5', '1', '9', '7']
T = [(input()) for _ in range(4)]
print(T)
# def Right(lst):
#     #리스트 뒤쪽에 앞의 4개의 요소 추가
#     for i in range(4):
#         lst.append(lst[i])
#     #리스트 앞쪽의 4개의 요소 제거
#     for _ in range(4):
#         lst.pop(0)
#
# def left(lst):
#     lst.append(lst[0]) #리스트 맨 앞의 요소를 맨 뒤에 추가
#     lst.pop(0) #리스트 맨 앞의 요소를 제거
#
# for i in range(4):
#     if T[i] == 'R':
#         Right(arr)
#     if T[i] == 'l':
#         left(arr)
# print(*arr)