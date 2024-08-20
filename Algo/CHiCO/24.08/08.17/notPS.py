def remove_numbers_to_avoid_PS(s):
    # 숫자를 제거한 후 문자열을 다시 체크
    candidates = []

    def dfs(current, index):
        # "PS4" 또는 "PS5"가 있는지 체크
        if "PS4" in current or "PS5" in current:
            return
        # 문자열의 끝에 도달했으면 후보로 저장
        if index == len(s):
            candidates.append(current)
            return
        # 현재 숫자를 무시하고 다음으로 넘어감
        if s[index].isdigit():
            dfs(current, index + 1)
        # 숫자를 포함하거나 포함하지 않는 두 경우를 모두 체크
        dfs(current + s[index], index + 1)

    # 초기 호출
    dfs("", 0)

    # 가장 긴 후보 반환
    return max(candidates, key=len)

# 입력 받기
N = int(input())
s = input().strip()

# 결과 출력
result = remove_numbers_to_avoid_PS(s)
print(result)
