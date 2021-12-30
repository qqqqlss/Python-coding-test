def solution(answers):
    a_1 = [1,2,3,4,5]
    a_2 = [2,1,2,3,2,4,2,5]
    a_3 = [3,3,1,1,2,2,4,4,5,5]
    count=[0,0,0]
    answer=[]
    count[0]=solve(answers,a_1)
    count[1]=solve(answers,a_2)
    count[2]=solve(answers,a_3)
    for i in range(3):
        if count[i]==max(count):
            answer.append(i+1)
    return answer

def solve(answers,a):
    cc=0
    c=0
    for i in range(len(answers)):
        if answers[i]==a[cc]:
            c=c+1
        cc+=1
        cc=cc%len(a)
    return c
"""
    def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
"""