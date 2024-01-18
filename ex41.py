# 푸드 파이트 대회

def solution(food):
    answer = []
    for i in range(1,len(food)):
        answer.append([i for j in  range(0, int(food[i] / 2))])
    tmp = sum(answer, [])
    tmp.append(0)
    rev_ans = tmp[:]
    rev_ans.sort(reverse=True)
    for i in range(len(rev_ans) - 1):
        tmp.append(rev_ans[i])
    answer = ''
    for i in range(len(tmp)):
        answer += str(tmp[i])
    return answer

def main():
    food = list(map(int, input().split()))
    print(solution(food))

if __name__ == "__main__":
    main()