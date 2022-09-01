def solution(brown, yellow):
    y=0
    for x in range(1,yellow+1):
        if yellow%x==0:
            y=yellow/x
            if brown==(2*x+2*y+4):
                if x>=y:
                    return [x+2,y+2]
                else:
                    return [y+2,x+2]