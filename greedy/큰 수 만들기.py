def solution(number, k):
    count=0
    idx=0
    while 1:
        if idx==len(number)-1:
            number=number[:idx]
            count+=1
            idx-=1
            if count==k:
                return number
        elif number[idx]<number[idx+1]:
            number=number[:idx]+number[idx+1:]
            count+=1
            if idx!=0:
                idx-=1
            if count==k:
                return number
        else:
            idx+=1
number="1924"
k=2
print(solution(number,k))