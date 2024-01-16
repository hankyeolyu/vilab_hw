# 약수의 합

def solution(n):
    answer = 0
    i = 1
    while n >= i:
        if n % i == 0:
            answer += i
        i += 1
    return answer

def main():
    n = int(input())
    print(solution(n))

if __name__ == "__main__":
    main()