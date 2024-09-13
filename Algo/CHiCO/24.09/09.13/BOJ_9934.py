def solve():
    K = int(input())  # 트리의 깊이
    buildings = list(map(int, input().split()))  # 상근이가 방문한 빌딩의 번호들 (중위 순회 결과)

    def build_levels(buildings, depth):
        if not buildings:
            return []
        mid = len(buildings) // 2
        left = build_levels(buildings[:mid], depth + 1)
        right = build_levels(buildings[mid + 1:], depth + 1)
        return [[buildings[mid]]] + merge_levels(left, right)

    def merge_levels(left, right):
        result = []
        for l, r in zip(left, right):
            result.append(l + r)
        result.extend(left[len(right):])
        result.extend(right[len(left):])
        return result

    levels = build_levels(buildings, 0)

    for level in levels:
        print(' '.join(map(str, level)))

solve()
