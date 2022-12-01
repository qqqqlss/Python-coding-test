def solution(survey, choices):
    answer = ''
    spec =[('R','T'),('C','F'),('J','M'),('A','N')]
    d=dict()
    
    for f,s in spec:
        d[f]=0
        d[s]=0
    
    for s,c in zip(survey,choices):
        if 1<=c<=3: #1->3 2->2 3->1  s[0]
            d[s[0]]+=4-c
        elif 5<=c<=7: #5->1 6->2 7->3   s[1]
            d[s[1]]+=c-4

    for f,s in spec:
        if d[f]>=d[s]:
            answer+=f
        else:
            answer+=s
            
    return answer