def solution(arr):
    first = arr[0][0]
    tf=True
    queue=[]
    answer=[0,0]
    for x in range(len(arr)):
        for y in range(len(arr)):
            if arr[x][y]!= first:
                tf=False
                break
        if tf==False:
            break
    if tf:
        if first==0:
            answer[0]+=1
        else:
            answer[1]+=1
        return answer
    else:
        queue=[arr]
    while queue: 
        table=queue.pop(0)
        if len(table)==1:
            if table[0]==0:
                    answer[0]+=1
            else:
                    answer[1]+=1
            continue
        d=int(len(table)/2)
        se=[[0,d,0,d],[d,2*d,0,d],[0,d,d,2*d],[d,2*d,d,2*d]] #네 등분 범위 정의
        for i in range(4):
            first=table[se[i][0]][se[i][2]]
            idx=[]
            tf=True
            for x in range(se[i][0],se[i][1]):
                idx_2=[]
                for y in range(se[i][2],se[i][3]):
                    if table[x][y]!= first:
                        tf=False
                    idx_2.append(table[x][y])
                idx.append(idx_2)
            if tf:  #압축되면 answer에서 추가
                if first==0:
                    answer[0]+=1
                else:
                    answer[1]+=1
            else: #압축 안되면 queue에 추가
                queue.append(idx)
    return answer

############  이게 더 빠름
def solution(arr):
    answer = [0, 0]

    def check(size, x, y):
        if size == 1:
            answer[arr[y][x]] += 1
            return
        else:
            first = arr[y][x]

            for dy in range(size):
                for dx in range(size):
                    if first != arr[y + dy][x + dx]:
                        check(size // 2, x, y)
                        check(size // 2, x + size // 2, y)
                        check(size // 2, x, y + size // 2)
                        check(size // 2, x + size // 2, y + size // 2)
                        return
            answer[first] += 1
    check(len(arr),0,0)
    return answer

arr=[[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
print(solution(arr))