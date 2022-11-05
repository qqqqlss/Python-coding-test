#import sys로 재귀 깊이 제한 안한거 (더 빠름 but 공간은 더 많이 씀)
def solution(n, lighthouse):
    answer = 0
    node_count = {i+1: [] for i in range(n)}

    for line in lighthouse:
        node_count[line[0]].append(line[1])
        node_count[line[1]].append(line[0])

    remain = n-1
    while remain > 0:
        for i in list(node_count.keys()): 
            if i in node_count and len(node_count[i]) == 1: #1개만 연결된거 불켬
                l_node = node_count[i][0]
                answer += 1
                for node in node_count[l_node]:
                    if len(node_count[node]) == 1:
                        del node_count[node]
                    else:
                        node_count[node].remove(l_node)
                remain -= len(node_count[l_node])
                del node_count[l_node]

    return answer


###dfs 재귀 깊이 제한 풀기
import sys
def dfs(node, conn, visited):
    visited[node] =True
    children = [next_node for next_node in conn[node] if not visited[next_node]]
    pick, not_pick=1, 0
    if not children: #leaf node
        return pick,not_pick
    else:
        for child in children:
            child_pick, child_not_pick=dfs(child, conn, visited)
            # 자식 고르지 않았으면 무조건 나를 골라야함
            # 자식을 골랐다면 나를골라도 되고 안 골라도 됨
            pick+=min(child_pick, child_not_pick)
            not_pick += child_pick
        return (pick, not_pick)

def solution(n, lighthouse):
    sys.setrecursionlimit(100000)
    conn =[[] for _ in range(n+1)]
    for a,b in lighthouse:
        conn[a].append(b)
        conn[b].append(a)
    visited = [False for _ in range(n+1)]
    root =1
    result= dfs(root, conn, visited)

    return min(result)


