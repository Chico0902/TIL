arr = input()
m_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in m_list:
    arr = arr.replace(i, 'i')
print(len(arr))