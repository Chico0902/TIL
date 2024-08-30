from itertools import product
N, M = map(int, input().split())

arr = list(range(1,N+1))
pro = list(product(arr,repeat=M))

for i in pro:
    print(*i)


# 백트래킹으로 풀기

def backtracking(N, M, sequence):
    # 현재 수열의 길이가 M이 되면 출력하고 재귀 종료
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return

    # 1부터 N까지의 수를 차례대로 사용하여 수열을 생성
    for i in range(1, N + 1):
        # 같은 수를 여러 번 선택할 수 있으므로 방문 체크는 필요 없음
        sequence.append(i)  # 숫자 추가
        backtracking(N, M, sequence)  # 재귀 호출
        sequence.pop()  # 마지막에 추가한 숫자 제거 (백트래킹)

# 입력 받기
N, M = map(int, input().split())

# 백트래킹 함수 호출
backtracking(N, M, [])
