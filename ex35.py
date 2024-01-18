# 크기가 작은 부분문자열

def solution(t, p):
    answer = 0
    for i in range(0, len(t) - len(p) + 1):
        tmp = t[i:i + len(p)]
        if int(tmp) <= int(p):
            answer += 1
    return answer

def main():
    t = input()
    p = input()
    print(solution(t, p))

if __name__ == "__main__":
    main()