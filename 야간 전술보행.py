def solution(distance, scope, times):
    t=0 #시간=위치
    idx=0 #경비 구간
    sc_ti=[] #scope+times
    for i in range(len(scope)): #묶어서 정렬 위해
        if scope[i][0]<scope[i][1]:
            sc_ti.append([scope[i][0],scope[i][1],times[i][0],times[i][1]])
        else:
            sc_ti.append([scope[i][1],scope[i][0],times[i][0],times[i][1]])
    sc_ti.sort()
    while t<distance:
        t+=1
        if sc_ti[idx][0]<=t and sc_ti[idx][1]>=t: #진입
            status=(t-1)%(sc_ti[idx][2]+sc_ti[idx][3])
            if status<sc_ti[idx][2]: #근무중 발각
                break    
        if sc_ti[idx][1]==t: #경비 X
            idx+=1
            if idx==len(scope):
                return distance        
    return t

######################## 훨씬 빠름
def solution(distance, scope, times):
    answer = 0
    s = sorted(zip(scope,times),key = lambda x : min(x[0]))
    for tmp,time in s:
        front,back = min(tmp),max(tmp)
        p = sum(time)
        for x in range(front,back+1):
            if x%p > 0 and x%p <= time[0]:
                return x
            else:
                continue
    return distance