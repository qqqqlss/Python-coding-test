def solution(dots):
    xx=0
    s=set()
    for i in range(len(dots)):
        if dots[i][0]-dots[i-1][0]==0:
            xx+=1
        else:
            s.add((dots[i][1]-dots[i-1][1])/(dots[i][0]-dots[i-1][0]))
    if len(s)<4 or xx>=2:
        return 1
    else:
        return 0

# combinations 사용
from itertools import combinations

def solution(dots):
    a = []
    for (x1,y1),(x2,y2) in combinations(dots,2):
        a.append((y2-y1,x2-x1))

    for (x1,y1),(x2,y2) in combinations(a,2):
        if x1*y2==x2*y1:
            return 1
    return 0
