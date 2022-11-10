from math import gcd
def solution(arrayA, arrayB):
    answer=[0]
    gcdA =arrayA[0]
    gcdB =arrayB[0]
    for i in range(1,len(arrayA)):
        gcdA=gcd(gcdA,arrayA[i])
        gcdB=gcd(gcdB,arrayB[i])
    tf=True
    for i in range(len(arrayA)):
        if arrayB[i]%gcdA==0:
            tf=False
            break
    if tf:
        answer.append(gcdA)
    tf=True
    for i in range(len(arrayA)):
        if arrayA[i]%gcdB==0:
            tf=False
            break
    if tf:
        answer.append(gcdB)
    return max(answer)