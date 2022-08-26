def solution(progresses, speeds):
    leng = len(speeds)
    stack = 0
    tf = False
    answer = []
    count = 0
    n = 0
    while stack!=leng:
        for i in range(leng):
            progresses[i]=progresses[i]+speeds[i]
        for i in range(stack,leng):
            if progresses[i] < 100:
                break
            if progresses[i] >= 100:
                stack=stack+1
                n=n+1
                tf = True
        if tf == True:
            print(progresses)
            answer.insert(count,n)
            count=count+1
        n = 0
        tf = False
    return answer
"""
    def solution(progresses, speeds):
        Q=[]
        for p, s in zip(progresses, speeds):
            if len(Q)==0 or Q[-1][0]<-((p-100)//s):
                Q.append([-((p-100)//s),1])
            else:
                Q[-1][1]+=1
        return [q[1] for q in Q]
"""