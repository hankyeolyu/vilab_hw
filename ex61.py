# 문자열 나누기

def solution(s):
    answer = 0
    count_x = 0
    count_xx = 0
    x = s[0]
    for c in s: 
        if count_x == count_xx:
            answer += 1
            x = c
            
        if c == x:
            count_x += 1
        else:
            count_xx += 1

    return answer