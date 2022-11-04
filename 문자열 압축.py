def solution(s):
    l=len(s)
    answer = l
    for i in range(1,int(l/2)+1):
        start=0
        tmp_str=s[start:start+i]
        count=1
        answer_str=''
        start+=i
        while start+i<l:
            if tmp_str==s[start:start+i]:
                count+=1
            else:
                if count==1:
                    answer_str+=tmp_str
                else:
                    answer_str+=str(count)+tmp_str
                tmp_str=s[start:start+i]
                count=1
            start+=i
        if tmp_str==s[start:]:
            count+=1
            answer_str+=str(count)+tmp_str
        else:
            if count==1:
                answer_str+=tmp_str+s[start:]
            else:
                answer_str+=str(count)+tmp_str+s[start:]
        answer=min(answer,len(answer_str))
    return answer