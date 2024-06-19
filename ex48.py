# 카드 뭉치

def solution(cards1, cards2, goal):
    answer = []
    len1 = len(cards1)
    len2 = len(cards2)
    
    i = 0
    j = 0
    for word in goal:
        if i < len1 and word == cards1[i]:
            answer.append(cards1[i])
            i += 1
        
        if j < len2 and word == cards2[j]:
            answer.append(cards2[j])
            j += 1
    
    if answer == goal:
        return 'Yes'
    else:
        return 'No'