def solution(topping):
    answer = 0
    a=set()
    b=set()
    first=[]
    for i in range(len(topping)-1,-1,-1):
        if topping[i] not in b:
            first.append(i)
            b.add(topping[i])
    first.sort()
    idx=0
    for i in range(len(topping)):
        a.add(topping[i])
        if i==first[idx]:
            b.remove(topping[i])
            idx+=1
        if len(a)==len(b):
            answer+=1
        elif len(a)>len(b):
            break
    return answer

topping=[1, 2, 1, 3, 1, 4, 1, 2]
print(solution(topping))

############# counter 사용
from collections import Counter

def solution(topping):
    answer = 0
    dic = Counter(topping)
    set_dic = set()
    answer = 0

    for i in topping:
        dic[i] -= 1
        set_dic.add(i)
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(set_dic):
            answer += 1

    return answer

############### defaultdict 사용
from collections import defaultdict

def solution(topping):
    first, second = defaultdict(int), set()
    count = 0
    for i in topping:
        first[i] = first[i] + 1
    for i in topping:
        first[i] = first[i] - 1
        if first[i] == 0:
            del first[i]
        second.add(i)
        if len(second) == len(first):
            count = count + 1
        if len(second) > len(first):
            break
    return count