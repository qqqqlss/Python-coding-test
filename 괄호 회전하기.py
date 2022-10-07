def solution(s):
    answer = 0
    if first(s)==False:
        return answer
    if tr(s):
        answer+=1
    for _ in range(len(s)-1):
        s=s[1:]+s[0]
        if tr(s):
            answer+=1
    return answer
def first(s): #처음 숫자 맞지않으면 return 0
    a=0 #()
    b=0 #[]
    c=0 #{}
    for i in s[:]:
        if i=="(":
            a+=1
        elif i==")":
            a-=1
        elif i=="[":
            b+=1
        elif i=="]":
            b-=1
        elif i=="{":
            c+=1
        elif i=="}":
            c-=1
    if a==0 and b==0 and c==0:
        return True
    else:
        return False
def tr(s): #올바른 문자열인지 확인
    stack=[]
    for i in s[:]:
        if i=="(":
            stack.append(")")
        elif i=="[":
            stack.append("]")
        elif i=="{":
            stack.append("}")
        else:
            if stack==[]:
                return False
            elif stack.pop()!=i:
                return False
    return True