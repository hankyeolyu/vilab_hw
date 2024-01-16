# 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = []
    tmp = 0
    while n > 0:
        tmp = n % 10
        n = int((n - tmp) / 10)
        answer.append(tmp)
    return answer

def main():
    n = int(input())
    print(solution(n))
    

if __name__ == "__main__":
    main()