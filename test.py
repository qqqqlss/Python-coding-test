from itertools import product
def solution(user_id, banned_id):
    bdict= []
    answer=set()
    for i in range(len(banned_id)):
        tmp=[]
        for j in range(len(user_id)):
            if dif(user_id[j],banned_id[i]):
                tmp.append(j)
        bdict.append(tmp)
    for a in set(product(*bdict)):
        if len(set(a))==len(banned_id):
            answer.add(','.join(sorted(list(a)))
        print(answer)
    return 1

def dif(id1, bid):
    if len(id1)!=len(bid):
        return False
    else:
        for i in range(len(id1)):
            if bid[i]=='*':
                continue
            if id1[i]==bid[i]:
                continue
            else:
                return False
    return True