def solution(X, Y): #제일 빠름
    answer = ''
    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))
    if answer == '' :
        return '-1'
    elif answer[0]=='0':
        return '0'
    else :
        return answer

#counter (import Counter 보다 빠름) STR 리스트로 추가해서 나중에 join으로 합치는거보다 +=로 합치는게 훨씬 빠름.