# 짝수와 홀수

def solution(num):
    answer = ''
    if num % 2 == 0:
        answer = "Even"
    else:
        answer = "Odd"
    return answer

def main():
    num = int(input())
    print(solution(num))

if __name__ == "__main__":
    main()