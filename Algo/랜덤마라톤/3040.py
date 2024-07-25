from itertools import combinations

m_list = []
for _ in range(9):
    m_list.append(int(input()))

comlist = list(combinations(m_list,7))
for i in comlist:
    if sum(i) == 100:
        for ans in i:
            print(ans)