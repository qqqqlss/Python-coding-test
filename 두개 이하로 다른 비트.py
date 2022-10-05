def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(f(num))
    return answer

def f(x):
    xbin='0'+format(x,'b')
    result=''
    for i in reversed(range(len(xbin))):
        if xbin[i]=='0':
            if i==len(xbin)-1:  #마지막이 0일때 1로 바꿔줌 == 홀수면 1만 더하면 되는거여따..!
                result=xbin[:-1]+'1'
                break
            elif i+2<len(xbin): #나머지- 0나오면 1로 바꾸고 바로뒤는 0으로.
                result=xbin[:i]+'10'+xbin[i+2:]
                break
            else:   # i+2 리스트 크기 넘어갈 때
                result=xbin[:i]+'10'
                break
    return int('0b'+result,2) #2진수 문자열 10진수로 변환
numbers=[2,7]
print(solution(numbers))