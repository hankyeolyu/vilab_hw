# 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = []
    for i in range(0, len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()
    return answer

def main():
    arr = list(map(int, input().split()))
    divisor = int(input())
    print(solution(arr, divisor))

if __name__ == "__main__":
    main()