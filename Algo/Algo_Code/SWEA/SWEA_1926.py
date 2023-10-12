N = int(input())
cnt = 0
for i in range(1,N+1):
    for j in ['3','6','9']:
        if j in str(i):
            cnt +=1
    if not cnt:
        print(i,end=' ')
    else:
        print('-'*cnt,end=' ')
    cnt = 0