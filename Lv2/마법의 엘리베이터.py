# 재귀 이용(dfs).

answer=float("inf")
def solution(storey):
    global answer
    dfs(storey, 0)

    return answer

def dfs(storey, count):
    global answer
    if storey<10:
        answer=min(answer,count+storey, count+11-storey)
        return
    else:
        one=storey%10
        dfs(storey//10, count+one)
        dfs(storey//10+1, count+10-one)


## 더 빠르긴 함 ( 수학적 계산 )
def solution(storey):
    answer = 0

    while(storey!=0):
        n = storey%10
        num = 0
        if n < 5:
            num = n
            storey -= n
        elif n > 5:
            num = 10 - n
            storey += num
        else:
            num = 5

        if num == 5:
            _storey = storey // 10
            if _storey % 10 >= 5:
                storey += num
            elif _storey % 10 < 5:
                storey -= num
        storey = storey // 10
        answer += num
    return answer