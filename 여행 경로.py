tickets=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
answer=[]

def solution(tickets):
    for i in range(len(tickets)): #시작하는 티켓 경우의 수
        ans=[]
        s=tickets.copy()
        if tickets[i][0]=="ICN":
            ans.extend(s.pop(i))
            sol(ans,s)
    answer.sort()
    return answer[0]

#ans와 남은 배열!!
def sol(ans, remain):
    global answer
    for i in remain:
        ans_c=ans.copy()
        remain_c=remain.copy()
        if ans[-1]==i[0]:
            ans_c.append(i[1])
            remain_c.remove(i)
            if remain_c==[]:
                answer.append(ans_c)
            else:
                sol(ans_c,remain_c)
                
print(solution(tickets))