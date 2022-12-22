def solution(array):
    answer = 0
    st=''.join(map(str,array))
    for i in range(len(st)):
        if st[i]=='7':
            answer+=1
    return answer

#############   count 사용

def solution(array):
    return ''.join(map(str, array)).count('7')