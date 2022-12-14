def solution(numbers, hand):
    answer = ''
    d=dict()
    count=0
    for y in range(3):
        for x in range(3):
            count+=1
            d[count]=[x,y]
    d[0]=[1,3]
    lloc=[0,3]
    rloc=[2,3]
    for i in numbers:
        if i in {1,4,7}:
            answer=answer+'L'
            lloc=d[i]
        elif i in {3,6,9}:
            answer=answer+'R'
            rloc=d[i]
        else:
            l=dif_xy(lloc,d[i])
            r=dif_xy(rloc,d[i])
            if l<r:
                answer=answer+'L'
                lloc=d[i]
            elif r<l:
                answer=answer+'R'
                rloc=d[i]
            else:
                if hand[0]=='l':
                    answer=answer+'L'
                    lloc=d[i]
                else:
                    answer=answer+'R'
                    rloc=d[i]
    return answer
def dif_xy(loc1,loc2):
    return abs(loc1[0]-loc2[0])+abs(loc1[1]-loc2[1])