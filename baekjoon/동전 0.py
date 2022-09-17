#11047
N,K=map(int,(input().split()))

dong=[]
answer=0
for i in range(N):
    dong.append(int(input()))
for i in range(N-1,-1,-1):
    if K>=dong[i]:
        mock, K=divmod(K,dong[i])
        answer+=mock
        if K==0:
            print(answer)