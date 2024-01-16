# 자릿수 더하기

def solution(n):
    answer = 0
    while n > 0:
        answer += n % 10
        n = int((n - (n % 10)) / 10)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer

def main():
    N = int(input())
    print(solution(N))

if __name__ == "__main__":
    main()