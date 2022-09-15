import math
def solution(fees, records):
    car={}
    answer = []
    for s in records:
        temp = s.split() # 0 시간 1번호 2출입
        t=temp[0].split(':')
        time=int(t[0])*60+int(t[1])
        print(time)
        if temp[1] not in car:
            car[temp[1]]=time
        elif car[temp[1]]>=0:
            car[temp[1]]-=time
        else:
            car[temp[1]]+=time

    for c in sorted(car):
        t=car[c]
        if t>=0:
            t-=1439     
        answer.append(fee(-t,fees))

    return answer

def fee(t,fees): #fees 0기본 1기본요금 2단위시간 3단위요금
        t=t-fees[0]
        f=fees[1]
        if t<=0:
            return f
        else:
            return fees[3] * math.ceil(t/fees[2])+f

#차량마다 hash계산
#없으면 -시간기록
#있으면 시간-절대값
#들어왓을대(x->시간) 나갈때(+ -> -누적시간)  또들어왓을떄(- -> 들어온 시간-누적시간) 나갈떄(+->누적시간)
    

fees=[180, 5000, 10, 600]
records=["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees,records))