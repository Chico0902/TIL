nodes = [(1, 2), (1, 3), (1,4), (2, 5), (2, 6), (4, 7), (4, 8), (9, 10), (9, 11)]
s, e = (1, 10)

dit = {}
for i in range(1, 12):
    dit[i] = []

for y, x in nodes:
    dit[y].append(x)

print(dit)