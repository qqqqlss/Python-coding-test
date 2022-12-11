from heapq import heappush, heappop
def solution(n, k, enemy):
    answer = 0
    maxheap =[]
    for i in enemy:
        n-=i
        heappush(maxheap,-i)
        if n<0:
            if k>0:
                k-=1
                n-=heappop(maxheap)
            else:
                return answer
        answer+=1
    return answer