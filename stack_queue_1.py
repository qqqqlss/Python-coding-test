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