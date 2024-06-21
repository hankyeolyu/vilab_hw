def solution(k, m, score):
    answer = 0
    cnt = 0
    score.sort(reverse=True)
    for i in range(0, len(score)):
        cnt += 1
        if cnt == m:
            cnt = 0
            answer += score[i] * m
    return answer
