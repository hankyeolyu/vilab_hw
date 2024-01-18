# 이상한 문자 만들기

# def solution(s):
#     answer = ''
#     for i in range(len(s)):
#         for j in range(len(s[i])):
#             if j % 2 == 0:
#                 answer += s[i][j].upper()
#             else:
#                 answer += s[i][j].lower()
#         answer += ' '
            
#     return answer

# def main():
#     s = list(map(str, input().split()))
#     print(solution(s))

def solution(s):
    answer = ''
    index = 0
    for i in range(len(s)):
        if s[i] == ' ':
            answer += s[i]
            index = 0
            continue
        if index % 2 == 0:
            answer += s[i].upper()
        else:
            answer += s[i].lower()
        index += 1
    return answer

def main():
    s = input()
    print(solution(s))

if __name__ == "__main__":
    main()