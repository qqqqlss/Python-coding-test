def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        idx=1
        for c in s:
            if c in skill[idx:]:
                answer-=1
                break
            elif c==skill[idx-1]:
                idx+=1
                if idx>=len(skill):
                    break
        answer+=1
    return answer

##### 요것도 괜찮은 거 같음 참고
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)
        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1
    return answer