import bisect, itertools, collections
def solution(info, query):
    infomap = collections.defaultdict(list)
    binarys = list(itertools.product((True, False), repeat=4))
    for inf in info:
        inf = inf.split()
        for binary in binarys:
            key = ''.join([inf[i] if binary[i] else '-' for i in range(4)]) 
            infomap[key].append(int(inf[4]))
    for k in infomap.keys():
        infomap[k].sort()
    answers = []
    for q in query:
        l,_,p,_,c,_,f, point = q.split()
        key = ''.join([l,p,c,f])
        i = bisect.bisect_left(infomap[key], int(point))
        answers.append(len(infomap[key]) - i)
    return answers
###########################################################################################################
def solution(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:    #query문 경우의 수 미리 dict에 저장
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())
    for i in info:
        i = i.split()
        for a in [i[0], '-']:   #-나 같은 경우의수에 점수 추가 
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    for k in data: #이분 탐색 위해 데이터 정렬 
        data[k].sort()

    answer = []
    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:    #이분탐색 - 탐색이 끝나고 index l부터 find이상의 수가 있음
            mid = (r+l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid+1

        answer.append(len(pool)-l) 

    return answer
# 1. 하나의 info에서 나올 수 있는 16가지의 key를 만들어서 infomap[key]에 값을 추가해줍니다.
# 2. 이분탐색을 위해 infomap의 값들을 정렬합니다.
# 3. query의 값을 key로 만들고 이분탐색으로 point 이상의 값 개수를 구합니다.
info=["python frontend senior chicken 210","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 210","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 270"]
print(solution(info, query))