m_list = input()
l = len(m_list)
open_list = []
close_list = []
for i in range(l):
    if m_list[i] == '(':
        open_list.append(i)
        b_int = int(m_list[i-1])
    if m_list[i] == ')':
        close_list.append(i)
        now_len = (i-1)-int(open_list[-1])
        ans_len = now_len * b_int



def play():
    global m_list
    global ans_len
    plusnum = int(open_list[-1]) - 2 - int(open_list[-2])
    m_list = m_list[:open_list[-1]] + m_list[close_list[0]:]
    ans_len = plusnum + ans_len

for _ in range(len(open_list)):
    play()
print(ans_len)
# 포기


