def solution(food):
    answer = ''
    for i in range(len(food)):
        for j in range(food[i]//2):
            answer+=str(i)
    return answer+'0'+answer[::-1]