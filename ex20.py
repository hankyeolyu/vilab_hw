# 제일 작은 수 제거하기

def solution(arr):
    answer = []
    min = arr[0]
    for i in range(0, len(arr)):
        if min > arr[i]:
            min = arr[i]
    for i in range(0, len(arr)):
        if arr[i] != min:
            answer.append(arr[i])
    if len(answer) == 0:
        answer.append(-1)
    
    return answer

def main():
    arr = list(map(int, input().split()))
    print(solution(arr))

if __name__ == "__main__":
    main()