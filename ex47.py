# 추억 점수

import numpy as np

def solution(name, yearning, photo):
    answer = []
    name_dict = {}
    
    for i in range(len(photo)):
        sum = 0
        for j in range(0, len(name)):
            if name[j] in photo[i]:
                sum += yearning[j]
        answer.append(sum)
    
    return answer

def main():
    name = ["may", "kein", "kain", "radi"]
    yearning = [5, 10, 1, 3]
    photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
    
    print(solution(name, yearning, photo))

if __name__ == '__main__':
    main()