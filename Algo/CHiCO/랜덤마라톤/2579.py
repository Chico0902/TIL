
# arr을 이렇게 만들면 N이 3보다 작을때 처리 안해주면 인덱스 오류
N = int(input())
arr = [0]

for _ in range(N):
    arr.append(int(input()))

DP = [0]*301

if N == 1:
    print(arr[1])
elif N == 2:
    print(arr[1]+arr[2])
else:
    DP[1] = arr[1]
    DP[2] = arr[1]+arr[2]
    DP[3] = max(arr[1]+arr[3],arr[2]+arr[3])
    if N > 3:
        for i in range(1,N+1):
            DP[i] = max(DP[i-3]+arr[i-1]+arr[i],DP[i-2]+arr[i])
    print(DP[N])

