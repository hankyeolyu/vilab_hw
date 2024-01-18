# 에산

def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        budget -= d[i]
        answer += 1
        if budget < 0:
            answer -= 1
            break
    return answer

def main():
    d = list(map(int, input().split()))
    budget = int(input())
    print(solution(d, budget))

if __name__ == "__main__":
    main()