# 음양 더하기

def solution(absolutes, signs):
    answer = 0
    for i in range(0, len(absolutes)):
        if signs[i] == "true":
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

def main():
    absolutes = list(map(int, input().split()))
    signs = list(map(str, input().split()))
    print(solution(absolutes, signs))

if __name__ == "__main__":
    main()