def solution(s):
    num_list=s.split()
    max_v=int(num_list[0])
    min_v=int(num_list[0])
    for n in num_list[1:]:
        max_v=max(max_v,int(n))
        min_v=min(min_v,int(n))
    answer = str(min_v)+' '+str(max_v)
    return answer