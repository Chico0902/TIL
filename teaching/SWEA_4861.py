# #쉬운 버전
# T = input()
# if isp(T):
#     print(f'{T}는 회문')
# else:
#     print(f'{T}는 회문이 아니다')
# #-------------------------------------------------
# # 어려운버전
def find_p(N, M, arr):
    for i in range(N):
        #각 행에서 가능한 시작 위치, M길이의 회문을 찾기위해서 N-M의 우 ㅣ치까지만 시작점 고려
        for j in range(N - M + 1):
            #가로 회문 -> 시작점 j에서 길이 M만큼의 부분 문자열
            h = arr[i][j:j+M]
            # 세로 회문 -> 시작점 j에서 길이 M만큼의 부분 리스트
            # K행 i열의 문자를 가져오면 세로로 문자를 읽을 수 있다.
            v = [arr[k][i] for k in range(j, j+M)]
            # 회문인지 판별
            if h == h[::-1]:
                return h
            if v == v[::-1]:
                return v
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input())for _ in range(N)]
    result = find_p(N, M, arr)# 함수 호출 -> 회문찾기
    print(f'#{tc}', ''.join(result))
