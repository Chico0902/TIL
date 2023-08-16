import copy

doku = [1,2,3]
doku1 = copy.deepcopy(doku)
doku1[1] = 5
print(doku, doku1)