import heapq
def solution(n, times): # n 관람차 개수, times 이용객 이용하고 싶은 시간
    idx=0
    answer=[]
    for i in range(1,n+1):
        num=times.pop(0)
        if num%n==0:
            num+=i
        else:
            num=((num//n)+1)*n+i
        heapq.heappush(answer, num)
    while times:
        num=times.pop(0)
        if num%n==0:
            num=(num//n)*n
        else:
            num=((num//n)+1)*n
        num+=heapq.heappop(answer)
        heapq.heappush(answer, num)
    return max(answer)

n=3
times=[4,7,1,3,5,6,2]
print(solution(n,times))