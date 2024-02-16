import math
def solution(r1, r2):
    answer = 0
    d_r1 = math.sqrt(r1)
    d_r2 = math.sqrt(r2)
    print(d_r1)
    print(d_r2)
    for i in range(1,r2):
        for j in range(1,r2):
            if i < r1:
                if j < r1:
                    pass
            if i**2 + j**2 <= r2**2 and i**2 + j**2 >= r1**2:
                answer+=1
    answer *= 4
    print(answer,'cek')
    answer += 4*(r2-r1+1)
    return answer