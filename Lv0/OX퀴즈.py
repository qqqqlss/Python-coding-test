def solution(quiz):
    answer=[]
    for s in quiz:
        answer.append(cal(s))
    return answer
def cal(s):
    l = s.split(' ')
    if l[1]=='+':
        if int(l[0])+int(l[2])==int(l[4]):
            return 'O'
        else:
            return 'X'
    else:
        if int(l[0])-int(l[2])==int(l[4]):
            return 'O'
        else:
            return 'X'


############ eval, replace 사용해서 간단하지만 좀 느림
def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)

def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]