# 콜라 문제

def solution(a, b, n):
    answer = 0
    
    while n >= a:
        bottle = n % a
        n = (n//a) * b
        answer += n
        n += bottle

    return answer

def main():
    print(solution(2, 1, 20))

if __name__ == '__main__':
    main()