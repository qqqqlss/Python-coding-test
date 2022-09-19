from itertools import combinations
def solution(line): #[A,B,C] Ax+ By+ C=0
    answer = []
    dot=[]
    for (a,b,e),(c,d,f) in combinations(line,2):
        if  (a*d-b*c)!=0:
            x=(b*f-e*d)/(a*d-b*c)
            y=(e*c-a*f)/(a*d-b*c)
        else:
            continue
        if (x%1)==0 and (y%1)==0:
            dot.append((int(x),int(y)))
    dot.sort()
    min_x=dot[0][0]
    max_x=dot[-1][0]
    dot.sort(key=lambda x:x[1])
    min_y=dot[0][1]
    max_y=dot[-1][1]
    dot=set(dot)
    for y in reversed(range(min_y,max_y+1)):
        string=''
        for x in range(min_x, max_x+1):            
            if (x,y) in dot:
                string=string+'*'
            else:
                string=string+'.'
        answer.append(string)
    
    return answer

line=[[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
print(solution(line))

def getIntersection(line1,line2):
    A,B,E = line1
    C,D,F = line2
    if A*D - B*C == 0:
        return (None,None)
    return ((B*F-E*D)/(A*D-B*C), (E*C-A*F)/(A*D-B*C))
def isInteger(x,y):
    return x != None and int(x) == x and int(y) == y
def minXY(idx,lst):
    return int(min(lst,key=lambda x: x[idx])[idx])
def maxXY(idx,lst):
    return int(max(lst,key=lambda x: x[idx])[idx])
def solution(lines):
    answer = []
    intersections = set()
    n = len(lines)
    for idx1 in range(n):
        for idx2 in range(idx1+1,n):
            x,y = getIntersection(lines[idx1],lines[idx2])
            if isInteger(x,y):
                intersections.add((y,x))
    for x in range(maxXY(0,intersections),minXY(0,intersections)-1,-1):
        tmp = ""
        for y in range(minXY(1,intersections),maxXY(1,intersections)+1):
            tmp += "*" if (x,y) in intersections else "."
        answer.append(tmp)

    return answer