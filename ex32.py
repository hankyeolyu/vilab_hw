# 3진법 뒤집기

def solution(n):
    answer = ''
    while n > 0:
        n, m = divmod(n, 3)
        answer += str(m)
    return int(answer, 3)

def main():
    n = int(input())
    print(solution(n))

if __name__ == "__main__":
    main()