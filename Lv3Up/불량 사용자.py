# 매우 빠름 dfs
def combi(temp, number, calculate):
    global result
    if len(temp) == len(calculate):
        temp = set(temp)
        if temp not in result:
            result.append(temp)
        return
    else:
        for j in range(len(calculate[number])):
            if calculate[number][j] not in temp:
                temp.append(calculate[number][j])
                combi(temp, number+1, calculate)
                temp.pop()
result = []
def solution(user_id, banned_id):
    global result
    calculate = []
    for ban in banned_id:
        possible=[]
        for user in user_id:
            if len(ban) != len(user):
                continue
            else:
                count = 0
                for i in range(len(ban)):
                    if user[i] == ban[i]:
                        count+=1
                if count == len(ban)-ban.count('*'):
                    possible.append(user)
        calculate.append(possible)

    combi([], 0, calculate)
    return len(result)

##################
# re, permutations 이용 더 간단 ( 비교적 느림 )
import re
from itertools import permutations 

def solution(user_id, banned_id):
    n = len(banned_id)
    banned_id = [i.replace("*", ".") for i in banned_id]
    answer = []

    for i in permutations(user_id, n):
        lst = list(i)
        flag = True
        for j in range(n):
            if re.match(banned_id[j], lst[j]) and (len(banned_id[j]) == len(lst[j])) :
                continue 
            else:
                flag = False
                break
        if flag:
            if sorted(lst) not in answer:
                answer.append(sorted(lst))

    return len(answer) 