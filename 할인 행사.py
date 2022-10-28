def solution(want, number, discount):
    dic1= dict(zip(want,number)) #want + number
    dic2=dic1.copy() #dic1 초기화
    answer=0
    count=0 #10개 넘으면 += 아니면 -
    idx=0
    while idx<len(discount):
        if discount[idx] not in dic1:
            dic1=dic2.copy()
            count=0
            idx+=1
            continue
        if count>=10:
            dic1[discount[idx]]-=1
            dic1[discount[idx-10]]+=1
        else:
            dic1[discount[idx]]-=1
            count+=1
        if dic1[discount[idx]]==0:
            if max(dic1.values())==0:
                answer+=1
        idx+=1
    return answer

want=["banana", "apple", "rice", "pork", "pot"]
number=[3, 2, 2, 2, 1]
discount=["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print(solution(want, number, discount))