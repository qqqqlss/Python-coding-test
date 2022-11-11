def solution(k, m, score):
    answer = 0
    ls=len(score)
    if ls<m:
        return 0
    score.sort()
    for i in range(1,(ls//m)+1):
        answer+=score[-(i*m)]
    return answer*m