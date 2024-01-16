# 서울에서 김서방 찾기

def solution(seoul):
    answer = ''
    for i in range(0, len(seoul)):
        if seoul[i] == 'Kim':
            answer = '김서방은 ' + str(i) + '에 있다'
    return answer

def main():
    seoul = list(map(str, input().split()))
    print(solution(seoul))

if __name__ == "__main__":
    main()