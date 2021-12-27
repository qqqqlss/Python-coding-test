def solution(participant, completion):
    hs = dict()
    for i in participant:
        if i not in hs:
            hs[i] = 1
        else:
            hs[i] +=1
            
    for i in completion:
        hs[i] -=1
    
    for key ,val in hs.items():
        if val != 0:
            return key