### 가장 빠름
def solution(target):
    dyn = [[100000, 0] for col in range(target+1)] #dyn[target] 까지 answer저장
    dyn[0][0] = 0
    count = 0
    
    while target > 300: #50, 60 최소공배수까진 무조건 60낮추면 된다
        target -= 60
        count += 1

    for i in range(target):
        for j in range(1, 21):
            #타겟보다 커지면 계산할 필요 없음 / 
            #i에 싱글 더하기=대상 / 대상의 횟수가 더 크거나     / (횟수는 같은데 single,불 횟수가 더 적을 떄) 갱신 
            if i+j <= target and (dyn[i+j][0] > dyn[i][0] + 1 or (dyn[i+j][0] == dyn[i][0]+1 and dyn[i+j][1] < dyn[i][1]+1)):
                dyn[i+j][0] = dyn[i][0] + 1
                dyn[i+j][1] = dyn[i][1] + 1
            #더블
            if i+j+j <= target and dyn[i+j+j][0] > dyn[i][0] + 1:
                dyn[i+j+j][0] = dyn[i][0] + 1
                dyn[i+j+j][1] = dyn[i][1]
            #트리플
            if i+j+j+j <= target and dyn[i+j+j+j][0] > dyn[i][0] + 1 :
                dyn[i+j+j+j][0] = dyn[i][0] + 1
                dyn[i+j+j+j][1] = dyn[i][1]
            #50
        if i+50 <= target and (dyn[i+50][0] > dyn[i][0]+1 or (dyn[i+50][0] == dyn[i][0]+1 and dyn[i+50][1] < dyn[i][1]+1)):
            dyn[i+50][0] = dyn[i][0] + 1
            dyn[i+50][1] = dyn[i][1] + 1
    dyn[target][0] += count
    answer = dyn[target]
    return answer


### itertools 사용
import itertools
def solution(target):
    all = [50]
    all.extend(i for i in range(1,21))
    all.extend(i*2 for i in range(1,21))
    all.extend(i*3 for i in range(1,21))
    all = list(set(all))

    tot = 0
    
    while target >= 300:
        tot += 1
        target -= 60

    r = []
    for i in range(1,target+1): #회수 별로 target될때 까지 조합
        r = [v for v in itertools.combinations_with_replacement(all,i) if sum(v)==target]
        if len(r) > 0:
            break

    if (len(r)) == 0:
        return [tot, 0]
    
    ct = max([len([v for v in x if v <= 20 or v==50]) for x in r]) #싱글, 50 가장 많은 거

    answer = [len(r[0])+tot, ct]

    return answer


#### 재귀

import sys

sys.setrecursionlimit(10**6)
#전부
score_set = set()
score_set = score_set | set([i+1 for i in range(20)])
score_set = score_set | set([(i+1)*2 for i in range(20)])
score_set = score_set | set([(i+1)*3 for i in range(20)])
score_set.add(50)
score_arr = sorted(list(score_set), reverse=True)
#싱글,50
b_set = set([i+1 for i in range(20)]+[50])
b_arr = sorted(list(b_set), reverse=True)
#싱글, 50 제외
a_set = score_set-b_set
a_arr = sorted(list(a_set), reverse=True)


dp = {0: (0, 0)}
for i in b_set:
    dp[i] = (1, -1)
for i in a_set:
    dp[i] = (1, 0)


def solve(remain):
    global dp
    if remain in dp:
        return (dp[remain])
    if remain < 0:
        return (123456789, -1)
    result = (123456789, -1)
    for i in score_arr:
        bb = 0
        if i in b_set:
            bb += 1
        ta, tb = solve(remain-i)
        result = min(result, (ta+1, tb-bb))
    dp[remain] = result

    return result


def solution(target):
    a, b = solve(target)
    return [a, -b]