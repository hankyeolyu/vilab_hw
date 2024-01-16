# 문자열을 정수로 바꾸기

from math import *

def solution(s):
    answer = 0
    index = len(s) - 1
    m = 1
    while index > 0:
        answer += int(s[index]) * m
        m *= 10
        index -= 1
    if s[0].isdigit():
        answer += int(s[0]) * m
    else:
        if s[0] =='+':
            pass
        else:
            answer *= -1
    return answer

def main():
    s = input()
    answer = solution(s)
    print(answer)
    
if __name__== "__main__":
    main()