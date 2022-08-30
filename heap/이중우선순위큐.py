import heapq
def solution(operations):
    heap=[]
    heap_2=[]
    for i in operations :
        s=int(i[2:])
        if i[0]=="I" :
            heapq.heappush(heap,s)
            heapq.heappush(heap_2,(-s,s))
        elif i[0]=="D" :
            if len(heap)>=1:
                if s==1:
                    x=heapq.heappop(heap_2)
                    heap.remove(x[1])
                    heapq.heapify(heap)
                else :
                    x=heapq.heappop(heap)
                    heap_2.remove((-x,x))
                    heapq.heapify(heap_2)
    if len(heap)==0:
        return [0,0]
    else :
        return [(heapq.heappop(heap_2))[1],heapq.heappop(heap)]
        
s=["I 7","I 5","I -5","D -1"]
print(solution(s))