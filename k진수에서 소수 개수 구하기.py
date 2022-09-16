def solution(n, k):
    k_jinsu=""
    answer=0
    while n>=k:
        k_jinsu = str(n%k) + k_jinsu
        n//=k
    k_jinsu=str(n)+k_jinsu
    k_split = k_jinsu.split('0')
    for s in k_split:
        if s == '':
            continue
        elif sosu(int(s)):
             answer+=1
    return answer

def isprime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True
#n을 k진수로 변환
#str으로 0을 기준으로 split
#소수의 개수.