def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x : (x[col-1], -x[0]))
    answer= S_i(data,row_begin)
    for i in range(row_begin+1,row_end+1):
        answer^=S_i(data,i)
    return answer
def S_i(data,i):
    s=0
    for j in range(len(data[0])):
        s+=(data[i-1][j]%i)
    return s