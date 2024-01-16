# 하샤드 수

def solution(x):
    answer = True
    tmp = 0
    tmp_x = x
    while x > 0:
        n = x % 10
        x = int((x - n) / 10)
        tmp += n
    if tmp_x % tmp != 0:
        answer = False
    else:
        pass
    return answer

def main():
    x = int(input())
    print(solution(x))

if __name__ == "__main__":
    main()