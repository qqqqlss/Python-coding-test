import heapq
import math
def solution(jobs):
    t=0
    count = 0
    end = 0
    c = 0
    result = 0
    heap = []
    jobs.sort(key = lambda  x:x[0])
    print(jobs)
    while 1 :
        if count<len(jobs):
            while jobs[count][0]==t : #대기 큐로
                heapq.heappush(heap, [jobs[count][1],jobs[count][1]])
                count+=1
                if count == len(jobs) :
                    break
        if t>=end : #대기큐에서 제일 짧은거 실행
            if len(heap)>=1 :
                ex=heapq.heappop(heap)
                c+=1
                print(ex)
                end = t+ex[0]
                result +=ex[1]
                if c==len(jobs):
                    return math.trunc(result/c)
        if len(heap)>=1 :
            for i in range(len(heap)):
                heap[i][1]=heap[i][1]+1
        t+=1

jobs =[[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]
s  = solution(jobs)
print(s)