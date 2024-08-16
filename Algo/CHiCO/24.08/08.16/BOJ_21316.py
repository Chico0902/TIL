dic = {}
one, two, three = [], [], []
for _ in range(12):
	x, y = map(int,input().split())
	if x in dic:
		dic[x].append(y)
	else:
		dic[x] = [y]
	if y in dic:
		dic[y].append(x)
	else:
		dic[y] = [x]
for i in dic:
	if len(dic[i]) == 1:
		one.append(i)
	elif len(dic[i]) == 2:
		two.append(i)
	else:
		three.append(i)
for i in three:
	sum = 0
	for j in dic[i]:
		sum += len(dic[j])
	if sum == 6:
		print(i)
		break