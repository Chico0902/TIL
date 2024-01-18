N = int(input())
checkpoint = []
distancearr = []
alldistance = 0

for i in range(N):
    X, Y = map(int, input().split())
    checkpoint.append([X,Y])

for i in range(N-1):
    distance = abs(checkpoint[i][0] - checkpoint[i+1][0]) + abs(checkpoint[i][1] - checkpoint[i+1][1])
    distancearr.append(distance)
    alldistance += distance


ans = alldistance
for i in range(N-2):
    minusdistance = alldistance - distancearr[i] - distancearr[i+1] + abs(checkpoint[i][0] - checkpoint[i+2][0]) + abs(checkpoint[i][1] - checkpoint[i+2][1])
    if minusdistance < ans:
        ans = minusdistance
print(ans)