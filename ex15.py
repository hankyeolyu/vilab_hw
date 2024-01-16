# 콜라츠 추측

def solution(num):
    answer = 0
    while num != 1 and answer < 500:
        if num % 2 == 0:
            num /= 2
        else:
            num = num *3 + 1
        answer += 1
    if answer == 500:
        answer = -1
    return answer

def main():
    num = int(input())
    print(solution(num))

if __name__ == "__main__":
    main()