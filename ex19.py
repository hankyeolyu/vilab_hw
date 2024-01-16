# 핸드폰 번호 가리기

def solution(phone_number):
    answer = ''
    for i in range(0, len(phone_number)):
        if len(phone_number) - 4 > i:
            answer += '*'
        else:
            answer += phone_number[i]
    return answer

def main():
    phone_number = input()
    print(solution(phone_number))

if __name__ == "__main__":
    main()