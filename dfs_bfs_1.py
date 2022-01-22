answer = 0
def solution(numbers, target):
    ans(numbers, 0, 0, 0, target)
    ans(numbers, 0, 1, 0, target)
    return answer

def ans(numbers, count, pn, result,target):
    global answer
    if pn==0:
        result+=numbers[count]
    elif pn==1:
        result-=numbers[count]
    count+=1
    if count==len(numbers) and result==target:
        answer+=1
    elif count < len(numbers):
        ans(numbers, count, 0, result, target)
        ans(numbers, count, 1, result, target)