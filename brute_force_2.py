import math
nus=[]
ha=0
def solution(numbers):
    global nus,ha
    answer=0
    nb=[]
    ha=len(numbers)
    for i in range(ha):
        nb.append(int(numbers[i]))
    for i in nb:
        re(i,0,0,nb)
    nus=list(set(nus))
    for i in nus:
        if sosu(i):
            answer+=1
    return answer
    
def re(s,c,res,nb): # s 넣을 상수, c 카운트, res 결과
    global nus,ha
    res+=s*10**(c)
    t=nb[:]
    nus.append(res)
    t.remove(s)
    c+=1
    if c==ha:
        return
    for i in t:
        re(i,c,res,t)
                    
def sosu(x):
    if x==0 or x==1:
        return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    print(x)
    return True