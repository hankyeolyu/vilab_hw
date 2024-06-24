# 덧칠하기

def solution(n, m, section):
    answer = 0
    tmp = 0
    for i in range(0, len(section)):
        if tmp > section[i]:
            continue
        answer += 1
        tmp = section[i] + m
    return answer