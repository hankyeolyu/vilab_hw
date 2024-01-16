# 정수 제곱근 판별
from math import sqrt

def solution(n):
    answer = 0
    tmp = sqrt(n)
    if tmp % 1 != 0:
        return -1
    else:
        answer = int(pow(tmp + 1, 2))
    return answer

def main():
    n = int(input())
    print(solution(n))

if __name__ == "__main__":
    main()