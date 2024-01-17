# 문자열 내림차순으로 배치하기

def solution(s):
    answer = ''
    small_ans = []
    big_ans = []
    for i in range(0, len(s)):
        if s[i].islower() == True:
            small_ans.append(ord(s[i]))
        else:
            big_ans.append(ord(s[i]))
    small_ans.sort(reverse=True)
    big_ans.sort(reverse=True)
    for i in range(0, len(small_ans)):
        ch1 = chr(small_ans[i])
        answer += ch1
    for i in range(0, len(big_ans)):
        ch2 = chr(big_ans[i])
        answer += ch2
    return answer

def main():
    s = input()
    print(solution(s))

if __name__ == "__main__":
    main()