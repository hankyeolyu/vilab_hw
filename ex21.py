# 내적

def solution(a, b):
    answer = 0
    for i in range(0, len(a)):
        answer += a[i] * b[i]
    return answer

def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solution(a, b))

if __name__ == "__main__":
    main()