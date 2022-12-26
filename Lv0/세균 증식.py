# 내가한(비트시프트 사용)
def solution(n, t):
    answer = n * (1 << t)
    return answer


## 더 간단한 버전
def solution(n, t):
    return n << t


## 지수(제곱) 사용
def solution(n, t):
    return n*(2**t)