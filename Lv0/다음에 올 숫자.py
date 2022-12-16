def solution(common):
    plus=common[1]-common[0]
    if common[0]!=0:
        product=common[1]/common[0]
    if common[2]-common[1]==plus:
        return common[-1]+plus
    else:
        return common[-1]*product