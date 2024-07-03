# 성격 유형 검사하기

def solution(survey, choices):
    dic = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    
    for i in range(len(survey)):
        q = survey[i]
        score = choices[i]
        
        q_1 = q[0]
        q_2 = q[1]
        
        list_q = [3,2,1,0,1,2,3]
        idx = score - 1
        if idx < 3:
            dic[q_1] += list_q[idx]
        elif idx == 3:
            continue
        else:
            dic[q_2] += list_q[idx]
    
    answer = ''
    
    if dic['R'] >= dic['T']:
        answer += 'R'
    else:
        answer += 'T'
    
    if dic['C'] >= dic['F']:
        answer += 'C'
    else:
        answer += 'F'
        
    if dic['J'] >= dic['M']:
        answer += 'J'
    else:
        answer += 'M'
        
    if dic['A'] >= dic['N']:
        answer += 'A'
    else:
        answer += 'N'
        
    return answer
            