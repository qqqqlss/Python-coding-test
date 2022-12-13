def solution(triangle):
    a=[0 for i in range(len(triangle))]
    for i in range(len(triangle)):
        sub=a.copy()
        for j in range(i+1):
            if j==0:
                a[j]=triangle[i][j]+sub[j]
            elif j==i:
                a[j]=triangle[i][j]+sub[j-1]
            else:
                if sub[j]>=sub[j-1]:
                    a[j]=triangle[i][j]+sub[j]
                elif sub[j]<sub[j-1]:
                    a[j]=triangle[i][j]+sub[j-1]
    return max(a)
"""
def solution(triangle):
    answer = 0
    triangle = [[0] + i + [0] for i in triangle]
    print(triangle)
    for i in range(1, len(triangle)):
        for j in range(1, i+2):
            triangle[i][j] = triangle[i][j] + max(triangle[i-1][j-1] , triangle[i-1][j])
            print(triangle[i][j])
            print(triangle[i-1][j-1] , triangle[i-1][j])
    answer = max(triangle[-1])
    return answer
"""