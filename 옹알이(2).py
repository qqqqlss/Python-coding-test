def solution(babbling):
    answer = 0
    three= ['aya','woo']
    two=['ye','ma']
    
    for s in babbling:
        idx=0
        idx_str=''
        tf=True
        while idx+3<=len(s):
            if s[idx:idx+3] in three:
                if s[idx:idx+3] == idx_str:
                    tf=False
                    break
                idx_str=s[idx:idx+3]
                idx+=3
            elif s[idx:idx+2] in two:
                if s[idx:idx+2] == idx_str:
                    tf=False
                    break
                idx_str=s[idx:idx+2]
                idx+=2
            else:
                tf=False
                break
        if tf:
            if (s[idx:] in two+three or s[idx:]=='') and s[idx:]!=idx_str:
                answer+=1
    return answer