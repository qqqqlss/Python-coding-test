def connect(lst, i, adj):
    stack = []
    for i in lst:
        stack.append(i)
    visit = [0]*len(adj)
    visit[i-1] = 1
    while stack:
        a = stack.pop()
        for i in adj[a-1]:
            if not visit[i-1]:
                stack.append(i)
                visit[i-1] = 1
    
    return visit

def solution(n, wires):
    adj = [[] for _ in range(n)] #송전탑 별 연결된 송전탑 리스트
    
    for a, b in wires:
        adj[a-1].append(b)
        adj[b-1].append(a)

    min_v = 100
    for i in range(n):
        for j in range(len(adj[i])):
            tmp = adj[i][j]
            adj[i].remove(adj[i][j]) # 연결 하나 빼서 ( 반대쪽 연결은 굳이 안빼도 연결안되면 방문 안함)
            if adj[i]:
                res = connect(adj[i], i, adj) # i기준 연결 조사
                min_v = min(min_v, abs(res.count(0) - res.count(1)))
            adj[i] = [tmp] + adj[i] #조사 후 다시 원상복구
    return min_v


#union find - 부모노드로 판별
uf = []

def find(a): #부모노드 찾기
    global uf
    if uf[a] < 0: return a
    uf[a] = find(uf[a])
    return uf[a]

def merge(a, b): #부모노드 통일..
    global uf
    pa = find(a)    #parent a
    pb = find(b)
    if pa == pb: return
    uf[pa] += uf[pb]
    uf[pb] = pa

def solution(n, wires):
    global uf
    answer = int(1e9) # 1* (10의 9승)  보통 2e9가 int 최대값 표현할떄 사용한다. 
    k = len(wires)
    for i in range(k):
        uf = [-1 for _ in range(n+1)]
        tmp = [wires[x] for x in range(k) if x != i]
        for a, b in tmp: merge(a, b)
        v = [x for x in uf[1:] if x < 0]
        answer = min(answer, abs(v[0]-v[1]))

    return answer