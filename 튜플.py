#더 빠름
def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))
                
    return answer

#############################내가 한
def solution(s):
    answer = []
    idx_str = ''
    tf=True
    entire=[]
    idx_list=[]
    count=0
    for st in s[1:-1]:
        if st=='{':
            tf=True
            continue
        elif st=='}':
            idx_list.append(int(idx_str))
            idx_str=''
            count+=1
            idx_list.insert(0,count)
            entire.append(idx_list)
            idx_list=[]
            count=0
            tf=False
        if tf:
            if st==',':
                idx_list.append(int(idx_str))
                idx_str=''
                count+=1
            else:
                idx_str+=st
    entire.sort()
    for i in entire:
        for j in i[1:]:
            if j not in answer:
                answer.append(j)
    return answer