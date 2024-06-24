# 실패율

def solution(N, stages):
    result = {}
    l = len(stages)
    for i in range(1, N + 1):
        if l != 0:
            cnt = stages.count(i)
            result[i] = cnt / l
            l -= cnt
        else:
            result[i] = 0
            
    return sorted(result, key=lambda x : result[x], reverse=True)