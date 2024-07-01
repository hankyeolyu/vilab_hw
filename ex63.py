# 대충 만든 자판

def solution(keymap, targets):
    answer = []
    dic = {}
    
    for st in keymap:
        for i in range(0, len(st)):
            c = st[i]
            if c not in dic:
                dic[c] = i + 1
            else:
                dic[c] = min(dic[c], i + 1)
    
    for st in targets:
        res = 0
        for c in st:
            if c in dic:
                res += dic[c]
            else:
                res = -1
                break
        answer.append(res)
    return answer