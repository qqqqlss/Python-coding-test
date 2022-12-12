def solution(routes):
    routes.sort()
    answer=1
    point=routes[0][1]
    for i in routes[1:]:
        if i[1]<point:
            point=i[1]
        elif i[0]>point:
            point=i[1]
            answer+=1
    return answer