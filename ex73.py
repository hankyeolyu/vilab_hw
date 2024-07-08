# 신규 아이디 추천

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word
            
    while '..' in answer:
        answer = answer.replace('..', '.')
    

    if answer[0] == '.':
        if len(answer) > 1:
            answer = answer[1:]
        else:
            answer = '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    
    if len(answer) == 0:
        answer = 'a'
    
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
            
    if len(answer) <= 3:
        answer += answer[-1] * (3- len(answer))
    
    return answer