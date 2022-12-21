def solution(my_str, n):
    answer = []
    c=0
    while c+n<=len(my_str):
        answer.append(my_str[c:c+n])
        c+=n    
    if c!=len(my_str):
        answer.append(my_str[c:])
    return answer