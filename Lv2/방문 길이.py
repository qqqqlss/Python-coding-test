def solution(dirs):
    x=0
    y=0
    row=set()
    col=set()
    for s in dirs:
        if s =='L':
            if x==-5:
                continue
            else:
                row.add((x-1,y,x,y))
                x-=1
        elif s=='R':
            if x==5:
                continue
            else:
                row.add((x,y,x+1,y))
                x+=1
        elif s=='U':
            if y==5:
                continue
            else:
                col.add((x,y,x,y+1))
                y+=1
        else:
            if y==-5:
                continue
            else:
                col.add((x,y-1,x,y))
                y-=1
    return len(row)+len(col)