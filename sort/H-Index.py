def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

# 정렬 활용안했음
# def solution(citations):
#     for i in range(len(citations)+2):
#         quote=0
#         for j in citations:
#             if j>=i:
#                 quote+=1
#         if quote<i:
#             return i-1