def solution(name):
    fin=[aton(name[i]) for i in range(len(name))]
    x=0
    ex=fin[:]
    answer=[]
    count=0
    for i in range(len(fin)): #오른쪽으로 쭉
        count+=ex[i]
        ex[i]=0
        if ex.count(0)==len(fin):
            answer.append(count)
        count+=1
    count=0
    ex=fin[:]
    for i in range(len(fin)): #왼쪽으로 쭉
        count+=ex[0-i]
        ex[0-i]=0
        if ex.count(0)==len(fin):
            answer.append(count)    
        count+=1+ex[0-i]
    ex=fin[:]
    count=0
    idx=0
    for i in range(len(fin)): #오른쪽 갔다가 왼쪽
        count+=ex[idx]
        ex[idx]=0
        if ex.count(0)==len(fin):
            answer.append(count)
        if ex[1:int(len(fin)/2)-1].count(0)==int(len(fin)/2)-2:
            idx-=1
            count+=1
        else:
            idx+=1
            count+=1
    ex=fin[:]
    count=0
    idx=0
    for i in range(len(fin)): #왼쪽 갔다가 오른쪽
        count+=ex[idx]
        ex[idx]=0
        if ex.count(0)==len(fin):
            answer.append(count)
        if ex[int(len(fin)/2)+2:].count(0)==len(fin)-int(len(fin)/2)-2:
            idx+=1
            count+=1
        else:
            idx-=1
            count+=1
    return min(answer)
def aton(a): #알파벳 별 스틱 수
    if ord(a)<=77:
        return ord(a)-65
    else:
        return 91-ord(a)