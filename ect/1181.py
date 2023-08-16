N = int(input())
my_list = []
for i in range(N):
    a = input()
    my_list.append(a)
# for k in range(N-1,0,-1):
#     for j in range(k):
#         if len(my_list[j]) > len(my_list[j+1]):
#             my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
#         elif len(my_list[j]) == len(my_list[j+1]):
#             if ord(my_list[j][0]) > ord(my_list[j+1][0]):
#                 my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
#
# A = list(set(my_list))
# print(A)


def new_list(words):
    sorted_list = list(set(words))
    n_list = sorted(sorted_list, key= lambda word: (len(word),word))
    return n_list

n_list = new_list(my_list)
for i in n_list:
    print(i)

