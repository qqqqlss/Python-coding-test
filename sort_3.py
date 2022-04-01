def solution(citations):
    for i in range(len(citations)+2):
        quote=0
        for j in citations:
            if j>=i:
                quote+=1
        if quote<i:
            return i-1