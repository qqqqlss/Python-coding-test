def solution(genres, plays):
    en=dict() #총재생
    fs=dict() #첫번째
    sc=dict() #두번째
    answer=[]
    for g,p in zip(genres,plays):
        if g not in en:
            en[g]=p
        else:
            en[g]+=p
        if g not in fs:
            fs[g]=p
        elif fs[g]<p:
            sc[g]=fs[g]
            fs[g]=p
        elif g not in sc:
            sc[g]=p
        elif sc[g]<p:
            sc[g]=p
    ensl=sorted(en.items(), key= lambda x : x[1],reverse=True) #총재생수 정렬리스트
    for a in ensl:
        if a[0] in fs:
            answer.append(plays.index(fs[a[0]]))
        if a[0] in sc:
            if plays.index(sc[a[0]]) in answer:
                ex=list(filter(lambda e:plays[e] == sc[a[0]], range(len(plays))))
                answer.append(ex[1])
            else:
                answer.append(plays.index(sc[a[0]]))
    return answer
'''
def solution(genres, plays):
    answer = []
    dic = {}
    album_list = []
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
        album_list.append(album(genres[i], plays[i], i))

    dic = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)
    album_list = sorted(album_list, reverse=True)



    while len(dic) > 0:
        play_genre = dic.pop(0)
        print(play_genre)
        cnt = 0;
        for ab in album_list:
            if play_genre[0] == ab.genre:
                answer.append(ab.track)
                cnt += 1
            if cnt == 2:
                break

    return answer

class album:
    def __init__(self, genre, play, track):
        self.genre = genre
        self.play = play
        self.track = track

    def __lt__(self, other):
        return self.play < other.play
    def __le__(self, other):
        return self.play <= other.play
    def __gt__(self, other):
        return self.play > other.play
    def __ge__(self, other):
        return self.play >= other.play
    def __eq__(self, other):
        return self.play == other.play
    def __ne__(self, other):
        return self.play != other.play    
'''