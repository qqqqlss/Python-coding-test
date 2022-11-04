def solution(k, ranges):
    answer = []
    sequence = []
    start=k
    while k!=1:
        if k%2==0:
            k/=2
        else:
            k=k*3+1
        end=k
        sequence.append(min(start,end)+abs(start-end)/2)
        start=k
    for x,y in ranges:
        if x>len(sequence)+y:
            answer.append(-1)
        elif y==0:
            answer.append(sum(sequence[x:]))
        else:
            answer.append(sum(sequence[x:y]))
    return answer