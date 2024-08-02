N = int(input())

ans = (N-1) + (N-1)*(N-2)
print(ans)
for i in range(2,N+1):
    print(1,i)