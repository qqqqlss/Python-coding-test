def solution(rows, columns, queries): 
    answer = []
    table=[]
    count=0
    for _ in range(rows): #row columns table
        t_row=[]
        for _ in range(columns):
            count+=1
            t_row.append(count)
        table.append(t_row)
    for x1,y1,x2,y2 in queries:
        row=x1-1  #현재 위치
        col=y1-1
        val=table[row][col]
        mini=val   #최소값
        for _ in range(y2-y1): #y1->y2
            col+=1
            tmp=table[row][col]
            table[row][col]=val
            val=tmp
            mini=min(val,mini)
        for _ in range(x2-x1): #x1->x2
            row+=1
            tmp=table[row][col]
            table[row][col]=val
            val=tmp
            mini=min(val,mini)
        for _ in range(y2-y1): #y2->y1
            col-=1
            tmp=table[row][col]
            table[row][col]=val
            val=tmp
            mini=min(val,mini)
        for _ in range(x2-x1): #x2->x1
            row-=1
            tmp=table[row][col]
            table[row][col]=val
            val=tmp
            mini=min(val,mini)
        answer.append(mini)
    return answer