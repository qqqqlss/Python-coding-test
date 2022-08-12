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
    adj = [[] for _ in range(n)]
    
    for a, b in wires:
        adj[a-1].append(b)
        adj[b-1].append(a)
    print(adj)
    min_v = 100
    for i in range(n):
        for j in range(len(adj[i])):
            tmp = adj[i][j]
            adj[i].remove(adj[i][j])
            if adj[i]:
                res = connect(adj[i], i, adj)
                min_v = min(min_v, abs(res.count(0) - res.count(1)))
            adj[i] = [tmp] + adj[i]
    return min_v


#union find
uf = []

def find(a):
    global uf
    if uf[a] < 0: return a
    uf[a] = find(uf[a])
    return uf[a]

def merge(a, b):
    global uf
    pa = find(a)
    pb = find(b)
    if pa == pb: return
    uf[pa] += uf[pb]
    uf[pb] = pa

def solution(n, wires):
    global uf
    answer = int(1e9)
    k = len(wires)
    for i in range(k):
        uf = [-1 for _ in range(n+1)]
        tmp = [wires[x] for x in range(k) if x != i]
        for a, b in tmp: merge(a, b)
        v = [x for x in uf[1:] if x < 0]
        answer = min(answer, abs(v[0]-v[1]))

    return answer