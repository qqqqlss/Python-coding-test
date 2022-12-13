from collections import defaultdict
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    d= dict()
    dd= defaultdict(set)
    for i in range(len(id_list)):
        d[id_list[i]]=i
    for s in report:
        a,b=s.split()
        dd[b].add(a)
    for v in dd.values():
        if len(v)>=k:
            for s in v:
                answer[d[s]]+=1
    return answer
# 한유저가 여러유저 신고
# k번 이상 신고받으면 정지 -> 신고한 유저에게 결과 메일 발송