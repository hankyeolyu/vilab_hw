# 완주하지 못한 선수

def solution(participant, completion):
    answer = ''
    participant = sorted(participant)
    completion = sorted(completion)
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    
    if len(answer) == 0:
        answer = participant[len(participant) - 1]
                
    return answer