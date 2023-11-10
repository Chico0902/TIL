T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    stop = [0] * 5001 # 1부터 5000까지 버스 정류장
    for i in range(N):
        Ai, Bi = map(int, input().split())
        #해당 정류정에 지나는 버스 대수 누적
        for j in range(Ai, Bi + 1):
            stop[j] += 1 #해당 정류장에 지나는 버스 노선 수
    P = int(input())
    result = []
    for j in range(P):
        Cj = int(input())
        result.append(stop[Cj]) #각 정류장에 지나는 버스 노선 수
    print(f'#{tc}', *result)