def solution(s):
    answer = 0
    idx=0
    check=s[0]
    for i in range(len(s)-1):
        if s[i]==check:
            idx+=1
        else:
            idx-=1
        if idx==0:
            answer+=1
            check=s[i+1]
    return answer+1