# 정수 내림차순으로 배치하기

def solution(n):
    answer = 0 
    arr = []
    m = 1
    while n > 0:
        tmp = n % 10
        n = int((n - tmp) / 10)
        arr.append(tmp)
    arr.sort()
    for i in range(0, len(arr)):
        answer += arr[i] * m
        m *= 10
    
    return answer

def main():
    n = int(input())
    print(solution(n))

if __name__ == "__main__":
    main()