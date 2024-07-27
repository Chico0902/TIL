def count_different_color_pairs(X, K, A):
    from collections import Counter
    
    # 왼발과 오른발 양말의 색 분포 계산
    left_socks = A[:X]
    right_socks = A[X:]
    
    left_counter = Counter(left_socks)
    right_counter = Counter(right_socks)
    
    # 전체 가능한 쌍의 수 계산
    total_left = sum(left_counter.values())
    total_right = sum(right_counter.values())
    total_pairs = total_left * total_right
    
    # 같은 색상의 쌍을 제외
    for color in range(1, K+1):
        if color in left_counter and color in right_counter:
            total_pairs -= left_counter[color] * right_counter[color]
    
    return total_pairs

# 입력받기
X, K = map(int, input().split())
A = list(map(int, input().split()))

# 결과 출력
result = count_different_color_pairs(X, K, A)
print(result)
