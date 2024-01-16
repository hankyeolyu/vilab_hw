# 자연수 뒤집어 배열로 만들기

def solution(s):
    answer = True
    cnt_p = 0
    cnt_y = 0
    
    for i in range(0, len(s)):
        if s[i].lower() == 'p':
            cnt_p += 1
        if s[i].lower() == 'y':
            cnt_y += 1
    if cnt_p != cnt_y:
        return False
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')

    return True

def main():
    s = input()
    print(solution(s))

if __name__ == "__main__":
    main()