def solution(n):
    array=[[0 for _ in range(i)] for i in range(1,n+1)]
    x,y=0,0
    count=1
    answer=[]
    while array[x][y]==0:
        array[x][y]=count
        while x+1<n and array[x+1][y]==0:
            x+=1
            count+=1
            array[x][y]=count
        while y+1<len(array[x]) and array[x][y+1]==0:
            y+=1
            count+=1
            array[x][y]=count
        while x-1>=0 and array[x-1][y-1]==0:
            x-=1
            y-=1
            count+=1
            array[x][y]=count
        if x+1<n:
            x+=1
            count+=1
    for i in array:
        answer.extend(i)
    return answer

print(solution(2))