def solution(n):
    answer = ''
    while n:
        if n % 3: #1,2 
            answer = str(n % 3) + answer 
            n //= 3
        else: #0
            answer = "4" + answer
            n = n//3 - 1
    return answer