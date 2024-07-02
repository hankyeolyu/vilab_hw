# 숫자 짝꿍

def solution(X, Y):
    answer = ''
    for i in range(0, 10):
        cnt1 = X.count(str(i))
        cnt2 = Y.count(str(i))
        for j in range(min(cnt1, cnt2)):
            answer += str(i)
    
    answer = sorted(answer, reverse=True)
    
    if len(answer) == 0:
        answer = '-1'
    elif len(answer) == answer.count('0'):
        answer = '0'
    else:
        answer = ''.join(answer)
    
    return answer