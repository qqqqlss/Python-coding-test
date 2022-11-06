from itertools import combinations
def solution(number):
    answer=0
    for x,y,z in combinations(range(len(number)),3):
        if number[x]+number[y]+number[z]==0:
            answer+=1
    return answer