def solution(bridge_length, weight, truck_weights):
    t = 0
    stack = 0 #트럭 시작
    stack_2 = 0 #트럭 끝
    bridge_weight = 0
    tt = [0 for i in range(len(truck_weights))] #시간저장 배열
    while 1 :
        t += 1
        if t == tt[stack_2] :
            bridge_weight -= truck_weights[stack_2]
            stack_2 += 1
        if bridge_weight + truck_weights[stack] <= weight :
            if stack == len(truck_weights)-1 :
                return t + bridge_length
            bridge_weight += truck_weights[stack]
            tt[stack] = t + bridge_length
            stack += 1