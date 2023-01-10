#내가 푼
def solution(s1, s2):
    s = len(s1)+len(s2)
    s12 = set(s1).union(set(s2))
    return s-len(s12)

# set 연산자 이용
def solution(s1, s2):
    return len(set(s1)&set(s2));

# in 이용
def solution(s1, s2):
    answer = 0

    for word in s1:
        if word in s2:
            answer += 1
        else:
            continue

    return answer