tickets=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
def solution(tickets):
    answer = [] 
    for i in range(len(tickets)): #시작하는 티켓 경우의 수
        s=tickets.copy()
        ans=[]
        if tickets[i][0]=="ICN":
            ans.extend(s.pop(i))
            answer.append(sol(ans,s, []))
    print(answer)
    #answer.sort()
    return 1

#ans와 남은 배열!!
def sol(ans, remain , answer):
    if not remain:
        return ans
    for i in range(len(remain)):
            if ans[-1]==remain[i][0]:
                sol(ans+[remain[i][1]],remain[:i]+remain[i+1:], answer)
    return ans

print(solution(tickets))

    