# 문자열 다루기 기본

def solution(s):
    answer = True
    for i in range(0, len(s)):
        if s[i].isdigit() == False:
            return False
    if len(s) != 4 and len(s) != 6:
        answer = False
    return answer

def main():
    s = input()
    print(solution(s))

if __name__ == "__main__":
    main()