# 나머지가 1이 되는 수 찾기

def solution(n):
    answer = 0
    x = 1
    while n > x:
        if n % x == 1:
            answer = x
            break
        else:
            pass
        x += 1
    return answer

def main():
    n = int(input())
    print(solution(n))

if __name__ == "__main__":
    main()