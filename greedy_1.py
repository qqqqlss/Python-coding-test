def solution(n, lost, reserve):
    answer=0
    a=[0 for i in range(n+2)]
    for i in range(1,n+1):
        a[i]+=1
        if i in lost:
            a[i]-=1
        if i in reserve:
            a[i]+=1
    for i in range(1,n+1):
        if a[i]==0 and a[i-1]==2:
            a[i]+=1
            a[i-1]-=1
            answer+=1
        elif a[i]==0 and a[i+1]==2:
            a[i]+=1
            a[i+1]-=1
            answer+=1
        elif a[i]>=1:
            answer+=1
    return answer