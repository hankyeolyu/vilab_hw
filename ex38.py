# 시저 암호

def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i].isalpha() == True:
            if s[i].islower() == True:
                answer += chr((ord(s[i]) + n) % ord('a') % 26 + ord('a'))
            else:
                answer += chr((ord(s[i]) + n) % ord('A') % 26 + ord('A'))
        else:
            answer += s[i]
        
    return answer

def main():
    s = input()
    n = int(input())
    print(solution(s,n))

if __name__ == "__main__":
    main()