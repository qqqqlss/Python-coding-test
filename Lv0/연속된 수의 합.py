def solution(num, total):
    answer = []
    fs=num*(num+1)/2
    gap=int((total-fs)/num)
    for i in range(gap+1,gap+num+1):
        answer.append(i)
    return answer