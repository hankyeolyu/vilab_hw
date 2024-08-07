# [PCCE 기출문제] 10번 / 데이터 분석

def solution(data, ext, val_ext, sort_by):
    answer = []
    ext_dict = {"code" : 0, "date" : 1, "maximum" : 2, "remain" : 3}
    
    for d in data:
        if d[ext_dict[ext]] < val_ext:
            answer.append(d)
    
    answer.sort(key=lambda x : x[ext_dict[sort_by]])
    
    return answer