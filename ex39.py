# 가장 가까운 같은 글자

def solution(s):
    answer = []
    cnt = [0 for i in range(0, 26)]
    index = [0 for i in range(0, 26)]
    for i in range(len(s)):
        if cnt[ord(s[i]) - ord('a')] == 0:
            answer.append(-1)
        else:
            answer.append(i - index[ord(s[i]) - ord('a')])
        cnt[ord(s[i]) - ord('a')] += 1
        index[ord(s[i]) - ord('a')] = i
        
    return answer

def main():
    s = input()
    print(solution(s))

if __name__ == "__main__":
    main()