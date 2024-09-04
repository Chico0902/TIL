# 내 풀이
arr = list(input())
ans_set = {}
N = len(arr)

for i in range(N):
    for j in range(N):
        if i+j+1 > N:
            break
        now = arr[i:i+j+1]
        now = "".join(now)
        if now in ans_set:
            continue
        else:
            ans_set[now] = 1

print(len(ans_set))


# 정답 코드
# 입력받기
S = input().strip()

unique_substrings = set()
    
# 문자열의 모든 시작점에 대해
for i in range(len(S)):
    # 부분 문자열을 확장
    for j in range(i + 1, len(S) + 1):
        substring = S[i:j]
        unique_substrings.add(substring)

# 고유한 부분 문자열의 개수 출력
print(len(unique_substrings))