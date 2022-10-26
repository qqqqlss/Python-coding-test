def solution(cards):
    visit=set() #방문한
    groups=[]
    while True: #모두 방문할 때까지 반복
        group=define_group(cards,visit)
        if group=={}:
            break
        else:
            groups.append(len(group))
            visit=visit.union(group)
    groups.sort(reverse=True)
    if len(groups)==1:
        return 0
    else:
        return groups[0]*groups[1]
def define_group(cards,visit): #방문 안 한 그룹 구하기
        group=set()
        first=-1
        if len(cards)==len(visit):
            return {}
        for i in range(len(cards)):
            if cards[i] not in visit:
                first=i
                break
        val=cards[first]
        group.add(val)
        while True: #first값 나올 때까지 반복
            val=cards[val-1]
            if val==cards[first]:
                break
            group.add(val)
        return group
cards=[8,6,3,7,2,5,1,4]
print(solution(cards))