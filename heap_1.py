import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    while heap[0] < K:
        if len(heap) >=2 : heap_min1 = heapq.heappop(heap)
        if len(heap) >=1 : heap_min2 = heapq.heappop(heap)
        heapq.heappush(heap, heap_min1 + (heap_min2*2))
        answer += 1
        if answer == len(scoville):
            return -1
    
    return answer
