def solution(s):
    count_0=0
    count_1=0
    while int(s)!=1:
        count=0
        for ss in s:
            if ss!='0':
                count+=1
            else:
                count_1+=1
        s=format(count, 'b')
        count_0+=1
    return [count_0,count_1]