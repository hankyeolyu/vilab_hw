# 문자열 내 마음대로 정렬하기

def solution(strings, n):
    strings.sort(key = lambda x : (x[n], x))
    
    return strings

def main():
    strings = ["sun", "bed", "car"]
    n = 1
    print(solution(strings, n))

if __name__ == '__main__':
    main()