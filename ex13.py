# 두 정수 사이의 합

def solution(a, b):
    answer = 0
    if a <= b:
        for i in range(a, b + 1):
            answer += i
    else:
        for i in range(b, a + 1):
            answer += i
    return answer

def main():
    a = int(input())
    b = int(input())
    print(solution(a, b))

if __name__ == "__main__":
    main()