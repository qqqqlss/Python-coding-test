def solution(sizes):
    x=0
    y=0
    for s in sizes:
        x=max(x,min(s)) #x축 길이
        y=max(y,max(s)) # y축 길이
    return x*y