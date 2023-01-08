def solution(num, k):
    snum=str(num)
    sk=str(k)
    if sk in snum:
        return snum.index(sk)+1
    else:
        return -1