# 없는 숫자 더하기

def solution(numbers):
    answer = 0
    cnt_arr = []
    for i in range(0, 10):
        cnt_arr.append(0)
    for i in range(0, len(numbers)):
        cnt_arr[numbers[i]] += 1
    for i in range(0, 10):
        if cnt_arr[i] == 0:
            answer += i
    return answer

def main():
    numbers = list(map(int, input().split()))
    print(solution(numbers))

if __name__ == "__main__":
    main()