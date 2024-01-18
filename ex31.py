# 같은 숫자는 싫어

def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(len(arr)):
        if i > 0:
            if arr[i-1] != arr[i]:
                answer.append(arr[i])
        else:
            answer.append(arr[i])
    return answer

def main():
    arr = list(map(int, input().split()))
    print(solution(arr))

if __name__ == "__main__":
    main()