from collections import defaultdict
from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    graph=defaultdict(list)
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)
    count=0
    queue=deque([])
    queue.append([destination,count])
    answer_dict=dict()
    while queue:
        idx,count=queue.popleft()
        if idx in answer_dict:
            continue
        else:
            answer_dict[idx]=count
        for i in graph[idx]:
            queue.append([i,count+1])
    for i in sources:
        if i in answer_dict:
            answer.append(answer_dict[i])
        else:
            answer.append(-1)
    return answer