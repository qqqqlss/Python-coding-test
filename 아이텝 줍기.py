def solution(rectangle, characterX, characterY, itemX, itemY):
    dot=[] #둘레 좌표 순서대로 저장.
    dot.extend(rec_to_dot(rectangle[0]))
    
    return find_distance(dot, characterX, characterY, itemX, itemY)

def rec_to_dot(rec): #직사각형 2꼭지점 -> 4꼭지점 반환
    return [[rec[0],rec[1]],[rec[0],rec[3]],[rec[2],rec[3]],[rec[2],rec[1]]]

def find_distance(dot, characterX, characterY, itemX, itemY): #dot, 캐릭터, 아이템 위치 통해 최소거리 찾기.
    dot.append(dot[0])
    round_len=0
    character_len=0
    item_len=0
    for i in range(len(dot)-1):
        if dot[i][0]==dot[i+1][0]: #세로 직선
            if dot[i][0]==characterX and characterY>=min(dot[i][1],dot[i+1][1]) and characterY<=max(dot[i][1],dot[i+1][1]):
                character_len = abs(dot[i][1]-characterY) + round_len
            if dot[i][0]==itemX and itemY>=min(dot[i][1],dot[i+1][1]) and itemY<=max(dot[i][1],dot[i+1][1]):
                item_len = abs(dot[i][1]-itemY) + round_len
            round_len += abs(dot[i][1]-dot[i+1][1])
        else: #가로 직선
            if dot[i][1]==characterY and characterX>=min(dot[i][0],dot[i+1][0]) and characterX<=max(dot[i][0],dot[i+1][0]):
                character_len = abs(dot[i][0]-characterX) + round_len
            if dot[i][1]==itemY and itemX>=min(dot[i][0],dot[i+1][0]) and itemX<=max(dot[i][0],dot[i+1][0]):
                item_len = abs(dot[i][0]-itemX) + round_len
            round_len += abs(dot[i][0]-dot[i+1][0])
    return min(abs(item_len-character_len), round_len-abs(item_len-character_len))

def add_dot(dot, rec): #테두리 점 집합에 사각형 추가
    

            
#직사각형 1-4개
#x또는 y 다 다름, 포함 관계 없음
#테두리 그리면서 사각형이랑 닿는 체크 좌표 추가.
#사각형 안에 들어가는 좌표 다삭제