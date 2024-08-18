def backtrack(n, m, nums, path):
    # 길이가 m인 수열을 완성했으면 출력
    if len(path) == m:
        print(" ".join(map(str, path)))
        return
    
    for i in range(n):
        if nums[i] not in path:
            path.append(nums[i])
            backtrack(n, m, nums, path)
            path.pop()  # 마지막 원소를 제거하여 다음 수열로 넘어감

# 입력 처리
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

# 백트래킹 호출
backtrack(n, m, nums, [])
