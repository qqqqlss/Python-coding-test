from itertools import permutations
def solution(expression):
    express=[]
    answer=[]
    idx=''
    for s in expression:    #문자열 분해->리스트
        if s=='+' or s=='-' or s=='*':
            express.append(int(idx))
            express.append(s)
            idx=''
        else:
            idx+=s
    express.append(int(idx))
    for s in permutations('+-*',3): #우선순위 순열
        express2=express.copy()
        for op in s:
            while op in express2: #op있으면 index찾아 계산
                idx_2 = express2.index(op)
                x=express2.pop(idx_2-1)
                express2.pop(idx_2-1)
                y=express2.pop(idx_2-1)
                result=0
                if op =='*':
                    result=x*y
                elif op=='-':
                    result=x-y
                else:
                    result=x+y
                express2.insert(idx_2-1, result)
        answer.append(abs(express2[0]))
    return max(answer)

expression="100-200*300-500+20"
print(solution(expression))