def solution(n, left, right):
    lm, lr=divmod(left,n)
    rm, rr=divmod(right,n)
    start_i=False
    start_j=False
    answer=[]
    for i in range(1,n+1):
        if i==lm+1:
            start_i=True
        if start_i:
            for j in range(1,n+1):
                if j==lr+1:
                    start_j=True

                if start_j:
                    if j<i:
                        answer.append(i)
                    else:
                        answer.append(j)
                if i==rm+1 and j==rr+1:
                    return answer

# 짧고 효율적 코드
def solution(n, left, right):
    answer = []

    for i in range(left, right+1):
        q, r = divmod(i, n)

        answer.append(max(q, r) + 1)

    return answer