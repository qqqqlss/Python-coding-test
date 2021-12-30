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
"""
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
"""