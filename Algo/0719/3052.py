s_list = [input() for _ in range(10)]

p_list = list(map(int,s_list))

n_list = []
for i in range(10):
    n_list.append(p_list[i]%42)

n_set = set(n_list)

print(len(n_set))