def solution(t, p):
    answer = 0
    for i in range(len(p),len(t)+1):
        if t[i-len(p):i]<=p:
            answer+=1  
    return answer