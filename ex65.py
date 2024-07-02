# 체육복

def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n + 1):
        if i in lost:
            if i in reserve:
                reserve.remove(i)
                lost.remove(i)
                
    answer = n - len(lost)
    
    for i in range(1, n + 1):
        if i in lost:
            if i - 1 in reserve:
                reserve.remove(i - 1)
                answer += 1
            elif i + 1 in reserve:
                reserve.remove(i + 1)
                answer += 1
        
    return answer