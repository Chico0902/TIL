def hwakga():
    for i in doku:
        check = []
        for j in i:
            if check:
                if j in check:
                    return 0
                else:
                    check.append(j)
            else:
                check.append(j)
    return 1


def hwakse():
    for i in range(9):
        dokuse = []
        for j in range(9):
            if dokuse:
                if doku[j][i] in dokuse:
                    return 0
                else:
                    dokuse.append(doku[j][i])
            else:
                dokuse.append(doku[j][i])
    return 1


def hwakne():
    for i in range(3):
        for j in range(3):
            dokumo = []
            for a in range(3):
                for b in range(3):
                    if dokumo:
                        if doku[i*3+a][j*3+b] in dokumo:
                            return 0
                    else:
                        dokumo.append(doku[i*3+a][j*3+b])
    return 1



T = int(input())

for tc in range(1, T+1):
    doku = [list(map(int, input().split()))for _ in range(9)]
    value_1 = hwakne()
    value_2 = hwakse()
    value_3 = hwakga()
    if value_1 == 1 and value_2 == 1 and value_3 == 1:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")