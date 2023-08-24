K = int(input())

D = []
S = []
N = []
B = []

for _ in range(6):
    BH, Giri = list(map(int, input().split()))
    if BH == 1:
        D.append(Giri)
    elif BH == 2:
        S.append(Giri)
    elif BH == 3:
        N.append(Giri)
    elif BH == 4:
        B.append(Giri)

big_s = sum(D) * sum(S)
small_s =
