def solution(k, d):
    answer = 0
    limit=int(d/k)
    j_limit=limit
    for i in range(limit+1):
        for j in range(j_limit,-1,-1):
            if (i*k)*(i*k)+(j*k)*(j*k)<= d*d:
                    answer+=j+1
                    j_limit=j
                    break
    return answer

# x - a*K / y = b*k / d넘으면 점 x
# a,b 0,1,2,3,~~