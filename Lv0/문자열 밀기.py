def solution(A, B):
    if A==B:
        return 0
    for i in range(1,len(A)):
        A=A[-1]+A[:-1]
        if A==B:
            return i
    return -1

##########################  문자열 붙이고 find 사용
solution=lambda a,b:(b*2).find(a)