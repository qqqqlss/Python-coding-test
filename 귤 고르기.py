from collections import Counter

def solution(k, tangerine):
    tc=Counter(tangerine)
    c=0
    answer=0
    #sorted(tc.values(), reverse = True) 도 가능
    for i in sorted(tc, key=tc.get, reverse=True):
        c+=tc[i]
        answer+=1
        if c>=k:
            break
    return answer