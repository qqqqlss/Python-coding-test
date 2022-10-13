from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    for c in course:
        str_list=defaultdict(lambda: 0)
        for i in range(len(orders)):
            combination_order=list(combinations(sorted(list(orders[i])),c))
            for comb in combination_order:
                str_list[''.join(comb)]+=1
        sort = sorted(str_list.items(), key = lambda item: -item[1])
        if sort!=[]:
            m = sort[0][1]
        for k,v in sort:
            if v==m and v>=2:
                answer.append(k)
            else:
                break
    answer.sort()
    return answer
##############################################################################

#좀더 깔끔
import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]