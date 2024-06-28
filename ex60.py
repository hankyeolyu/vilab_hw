# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    answer = []
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    count = 0
    zero = lottos.count(0)
    for i in lottos:
        for j in win_nums:
            if i == j:
                count += 1
    answer.append(rank[count + zero])
    answer.append(rank[count])
    return answer