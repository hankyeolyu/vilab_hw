# 부족한 금액 계산하기

def solution(price, money, count):
    answer = 0
    for i in range(1, count + 1):
        answer += price * i
    if money - answer < 0:
        answer -= money
    else:
        answer = 0    

    return answer

def main():
    price = int(input())
    money = int(input())
    count = int(input())
    print(solution(price, money, count))

if __name__ == "__main__":
    main()