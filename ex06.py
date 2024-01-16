# x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer = []
    i = 1
    tmp = x
    while n >= i:
        answer.append(tmp)
        tmp += x
        i += 1
    return answer

def main():
    x = int(input())
    n = int(input()) 
    print(solution(x, n))

if __name__ == "__main__":
    main()