def solution(array):
    answer=[]
    m=max(array)
    answer.append(m)
    answer.append(array.index(m))
    return answer