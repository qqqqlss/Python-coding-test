def solution(p):
    answer=first(p)
    return answer
def first(v):
    if v=='':
        return ''
    count=0
    tf=True
    u=''
    for i in range(len(v)):
        if v[i]=='(':
            count+=1
        else:
            count-=1
            if count<0:
                tf=False
        if count==0:
            u=v[:i+1]
            if i==len(v)-1:
                v=''
            else:
                v=v[i+1:]
            break
    if tf:
        return u+first(v)
    else:
        return '('+first(v)+')'+"".join(reversed(u[1:-1]))
p="(()())()"
print(solution(p))