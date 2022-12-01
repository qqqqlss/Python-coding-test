from itertools import product
def solution(clockHands):
    answer = int(1e9)
    n = len(clockHands)

    def calc(x, y): #상하좌우자신의 회전개수에 따라 현재 방향 계산
        dx = [0,0,0,1,-1]
        dy = [0,1,-1,0,0]
        temp = 0
        for k in range(5):
            nx = x + dx[k]
            ny = y + dy[k]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            temp += data[nx][ny]
        return (clockHands[x][y] + temp) % 4

    for li in product(list(range(4)), repeat=n):
        data = [[0] * n for _ in range(n)]  #회전수 저장
        data[0] = list(li).copy() #첫 행  바꾸는 경우의수 대입.
        for i in range(1, n):
            for j in range(n):
                data[i][j] = (4 - calc(i-1, j)) % 4 # 위에 행 True되도록 회전
        for j in range(n): #마지막 행 다른 방향 있으면 break
            if calc(n-1, j) != 0:
                break
        else: #마지막 행 모두 true
            temp = sum([sum(t) for t in data]) #data sum에서 총 회전수 계산
            answer = min(answer, temp) #총 회전수 작은거 저장.

    return answer
