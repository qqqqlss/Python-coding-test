import math
def solution(number, limit, power):
    answer = 0
    for n in range(1,number+1):
        result=0
        m=math.isqrt(n)
        if (m*m)==n:
            result+=1
        elif n%m==0:
            result+=2
        for i in range(1,m):
            if n%i==0:
                result+=2
            if result>limit:
                break
        if result>limit:
            answer+=power
        else:
            answer+=result
    return answer