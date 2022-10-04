dx=[0,1,0,-1] #시계방향
dy=[1,0,-1,0]

def solution(places):
    answer = []
    for i in range(5): #room N
        tf= False #거리 두리 안지키면 True
        for j in range(5): #x
            for k in range(5): #y
                if places[i][j][k]=='P': #사람일 떄
                    for l in range(4): #네방향탐색
                        x,y=j,k
                        if x+dx[l]>=0 and x+dx[l]<5 and y+dy[l] >=0 and y+dy[l]<5:
                            x=x+dx[l]
                            y=y+dy[l]
                            if places[i][x][y]=='P': #옆에 사람
                                tf=True
                                break
                            elif places[i][x][y]=='O': #옆에 책상
                                if x+dx[l]>=0 and x+dx[l]<5 and y+dy[l] >=0 and y+dy[l]<5:
                                    if places[i][x+dx[l]][y+dy[l]]=='P':
                                        tf=True
                                        break
                                if x+dx[l-1]>=0 and x+dx[l-1]<5 and y+dy[l-1] >=0 and y+dy[l-1]<5:
                                    if places[i][x+dx[l-1]][y+dy[l-1]]=='P':
                                        tf=True
                                        break
                            else: #옆에 칸막이
                                if x+dx[l-1]>=0 and x+dx[l-1]<5 and y+dy[l-1] >=0 and y+dy[l-1]<5:
                                    x=x+dx[l-1] #반시계
                                    y=y+dy[l-1]
                                    if places[i][x][y]=='P':
                                        x=x+dx[l-2] #반시계
                                        y=y+dy[l-2]
                                        if places[i][x][y]!='X':
                                            tf=True
                                            break
                    if tf:
                        break
            if tf:
                break
        if tf:
            answer.append(0)
        else:
            answer.append(1)
    return answer