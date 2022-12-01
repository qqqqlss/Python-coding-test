from heapq import heappush, heappop
def solution(k, score):
    hrecord = []
    answer = []
    for i in score:
        if len(hrecord)>=k:
            if i>hrecord[0]:
                heappop(hrecord)
                heappush(hrecord, i)
        else:
            heappush(hrecord, i)
        answer.append(hrecord[0])
    return answer