# 수학적으로 은근 머리 써야댐....훨씬 빠름
import math
def solution(w,h):
    answer = w*h
    gcd = math.gcd(w,h)
    a = w/gcd
    b = h/gcd
    return answer - gcd*(a+b-1)

## 내가 푼 ( 시간 오래 걸림 )
from math import floor,ceil,gcd
def solution(w,h):
    if w==1 or h==1:
        return 0
    count=0
    start=h
    end=0
    for i in range(1,int(w/gcd(w,h))+1):
        end=-(h/w)*i+h
        count+=ceil(start)-floor(end)
        start=end
    count*=gcd(w,h)
    return w*h-count