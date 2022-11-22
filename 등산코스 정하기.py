from collections import defaultdict
from collections import deque
def solution(n, paths, gates, summits):
    answer = [n+1,10000001]
    graph=defaultdict(list)
    for x,y,z in paths:
        graph[x].append([y,z])
        graph[y].append([x,z])
    gates=set(gates)
    summits=set(summits)
    for s in summits: # 산봉우리마다 최소값 구하기 / 출입구, 산봉우리 만나면 멈춤
        visit={}
        stack=deque()
        for x,y in graph[s]: #처음 산봉우리 돌기
            if y>answer[1]: #intensity보다 크면 넘김
                continue
            if x in gates: #gates 면 answer 갱신
                if answer[1]>y:
                    answer=[s, y]
                elif answer[0]>s:
                    answer[0]=s
            elif x in summits: #summits이면 넘김
                continue
            else: #쉼터 stack추가
                stack.append([x,y])
        while stack: #다방문할떄까지.
            loc,intensity=stack.popleft()
            if loc not in visit:
                visit[loc]=intensity
            else:
                if visit[loc]<=intensity:
                    continue
                else:
                    visit[loc]=intensity
            for x,y in graph[loc]:
                if y>answer[1] or (y==answer[1] and s>=answer[0]): #intensity보다 크면 넘김
                    continue
                if x in gates: #gates 면 answer 갱신
                    if answer[1]>=max(intensity,y):
                        answer=[s, max(intensity,y)]
                    elif answer[1]==max(intensity,y):
                        answer[0]=s
                elif x in summits: #summits면 넘김
                    continue
                else: #쉼터 stack 추가
                    stack.append([x,max(intensity,y)])
            #answer과 비교해서 갱신
    return answer