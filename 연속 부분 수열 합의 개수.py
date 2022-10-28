def solution(elements):
    answer = set()
    l=len(elements)
    elements=elements+elements
    for i in range(1,l+1):
        for j in range(l):
            e=sum(elements[j:j+i])
            answer.add(e)
    return len(answer)

elements=[7,9,1,1,4]	
print(solution(elements))