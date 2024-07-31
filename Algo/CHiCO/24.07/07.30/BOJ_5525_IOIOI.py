# 문제

"""
N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.

P1 IOI
P2 IOIOI
P3 IOIOIOI
PN IOIOI...OI (O가 N개)
I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.
"""

# 입력

# 첫째 줄에 N이 주어진다. 둘째 줄에는 S의 길이 M이 주어지며, 셋째 줄에 S가 주어진다.

# 출력

# S에 PN이 몇 군데 포함되어 있는지 출력한다.

# 정답

from collections import deque

N = int(input())
M = int(input())
S = deque(input())
findarr = 'IO'*N + 'I'
idx = 0
cnt = 0

def find(N, S, idx):
    global cnt
    flag = 0
    mididx = 0
    for i in range(N*2+1):
        if i%2 == 0:
            if S[idx+i] == 'I':
                continue
            else:
                flag = 1
                mididx = i
                break
        else:
            if S[idx+i] == 'O':
                continue
            else:
                flag = 1
                mididx = i
                break
    if flag == 0:
        cnt += 1
    return flag, mididx
    
def addfind(S, idx):
    look = 1
    addidx = 0
    while look:
        if addidx %2 == 0:
            if S[idx+addidx] == 'O':
                addidx += 1
            else:
                look = 0
                plusidx = addidx//2

        elif addidx%2 == 1:
            if S[idx+addidx] == 'I':
                addidx += 1
            else:
                look = 0
                plusidx = addidx//2
    return plusidx



print(idx,'idx1')
print(M,'M')
while idx < M:
    if idx < M:
        if S[idx] == 'O':
            idx += 1
            print(idx,'idx')
        else:
            flag, mididx = find(N, S, idx)
            print(mididx,'mididx')
            if flag == 0:
                idx += N
            else:
                idx += mididx
            plusidx = addfind(S, idx)
            idx += plusidx
            cnt += plusidx

print(cnt)