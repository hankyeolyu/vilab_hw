# 옹알이 (2)

def solution(babbling):
    answer = 0
    can_speak_word = ['aya', 'ye', 'woo', 'ma']
    for bab in babbling:
        for can in can_speak_word:
            if can * 2 not in bab:
                bab = bab.replace(can, ' ')
        if bab.isspace():
            answer += 1
        
    return answer