def solution(beginning, target):
    answer = 0
    table = [[beginning[i][j] ^ target[i][j] for j in range(len(beginning[i]))] for i in range(len(beginning))]
    cnt = 0
    m = len(table)
    n = len(table[0])
    
    for i in range(1, m):
        if (table[i] != table[0]):  #첫째열과 비교해서 같으면 +
            cnt+=1
            if (list(map(lambda x: x ^ 1, table[i])) != table[0]):
                return -1   #반전해서 다르면 못만듬.

    answer = min((cnt) + sum(table[0]), (m - cnt) + (n - sum(table[0])))
                #첫째열 통일 다른 열 바꿔주기 / 반전열 통일 다른열 바꿔주기       
    return answer
beginning=	[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
target=[[1, 0, 0, 0, 0], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1]]
print(solution(beginning, target))

