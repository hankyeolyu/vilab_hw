def solution(answers):
    answer = []
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    ans_1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    ans_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(0, len(answers)):
        if ans_1[i % 10] == answers[i]:
            cnt_1 += 1
        if ans_2[i % 8] == answers[i]:
            cnt_2 += 1
        if ans_3[i % 10] == answers[i]:
            cnt_3 += 1
    
    if cnt_1 >= cnt_2 and cnt_1 >= cnt_3:
        answer.append(1)
    if cnt_2 >= cnt_1 and cnt_2 >= cnt_3:
        answer.append(2)
    if cnt_3 >= cnt_1 and cnt_3 >= cnt_2:
        answer.append(3) 
    
    return answer