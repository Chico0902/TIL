#
print(eval(input()))

#덧셈기호를 기준으로 분리
word = input().split('+')
ans = any()
for w in word:
    #뺄셈 기호를 기준으로 분리
    w = w.split("-")
    #첫번째 요소는 더해줄 값
    inner_ans = int(w[0])
    #나머지 요소들은 빼줄 값
    for i in range(1, len(W)):
            inner_ans -= int(w[i])
    #이 부분의 결과의 전체 합계
    ans += inner_ans
print(ans)