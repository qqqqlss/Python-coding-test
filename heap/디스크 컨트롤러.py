# import heapq
# import math
# def solution(jobs):
#     t=0
#     count = 0
#     end = 0
#     c = 0
#     result = 0
#     heap = []
#     jobs.sort(key = lambda  x:x[0])
#     print(jobs)
#     while 1 :
#         if count<len(jobs):
#             while jobs[count][0]==t : #대기 큐로
#                 heapq.heappush(heap, [jobs[count][1],jobs[count][1]])
#                 count+=1
#                 if count == len(jobs) :
#                     break
#         if t>=end : #대기큐에서 제일 짧은거 실행
#             if len(heap)>=1 :
#                 ex=heapq.heappop(heap)
#                 c+=1
#                 print(ex)
#                 end = t+ex[0]
#                 result +=ex[1]
#                 if c==len(jobs):
#                     return math.trunc(result/c)
#         if len(heap)>=1 :
#             for i in range(len(heap)):
#                 heap[i][1]=heap[i][1]+1
#         t+=1

##이게 훨씬 빠름 
import heapq
from collections import deque

def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    print(tasks)
    q = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())
    return total_response_time // len(jobs)

jobs =[[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]
s  = solution(jobs)
print(s)