# 가운데 글자 가져오기

def solution(s):
    answer = ''

    if len(s) % 2 == 0:
        answer += s[int((len(s)-1)/2)]
        answer += s[int((len(s)+1)/2)]
    else:
        answer += s[int((len(s) - 1) /2)]
    return answer

def main():
    s = input()
    print(solution(s))

if __name__ == "__main__":
    main()