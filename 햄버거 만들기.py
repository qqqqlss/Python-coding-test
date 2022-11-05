def solution(ingredient):
    answer = 0
    queue =[]
    for i in ingredient:
        queue.append(i)
        if len(queue)>=4:
            while queue[-4:]==[1,2,3,1]:
                for _ in range(4): #queue=queue[-4:] 보다 훨씬 빠름
                    queue.pop()
                answer+=1
                if len(queue)<4:
                    break
    return answer
#1빵 2야채 3고기 1빵