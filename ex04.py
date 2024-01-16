# 평균 구하기

def solution(arr):
    answer = 0
    for i in range(0, len(arr)):
        answer += arr[i]
    answer /= len(arr)
    return answer

def main():
    arr = list(map(int, input().split()))
    print(solution(arr))

if __name__ == "__main__":
    main()