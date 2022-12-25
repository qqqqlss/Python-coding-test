def solution(my_string):
    my_string=my_string.lower()
    answer=[]
    for i in range(len(my_string)):
        answer.append(my_string[i])
    answer.sort()
    return ''.join(answer)

########### 이게 맞음
def solution(my_string):
    return ''.join(sorted(my_string.lower()))