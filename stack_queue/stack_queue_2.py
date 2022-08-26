def solution(priorities, location):
    answer = 0
    while 1:
        first=priorities[0]
        if max(priorities) > first:
            if priorities.index(max(priorities))==location:
                answer+=1
                return answer
            priorities.append(priorities.pop(0))
            if location==0:
                    location=len(priorities)-1
            else:
                    location-=1
        else:
            if location==0:
                answer+=1
                return answer
            priorities.pop(0)
            answer+=1
            location-=1