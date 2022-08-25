def solution(clothes):
    hs=dict()
    answer = 1
    for (a,b) in clothes:
        if b not in hs:
            hs[b]=2
        else:
            hs[b]+=1
    for key in hs:
        answer*=hs[key]
    return answer-1