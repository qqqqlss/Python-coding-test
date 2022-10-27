def solution(order):
    answer = 0
    n = len(order)
    box_idx=1
    sup=[]
    for i in order:
        if box_idx<i: #box번호까지 보조컨테이너에 up하며 실음 
            sup.extend([i for i in range(box_idx,i)])
            box_idx=i+1
            answer+=1
        elif box_idx==i: #box번호나오면 바로 실음
            box_idx+=1
            answer+=1
        else: #box번호 지났으면 sup컨테이너 확인 없으면 중단
            if sup[-1]==i:
                answer+=1
                sup.pop(-1)
            else:
                break
    return answer