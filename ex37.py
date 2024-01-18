# 최소 직사각형

def solution(sizes):
    big = max([max(i) for i in sizes])
    small = max([min(j) for j in sizes])
    answer = big * small
    return answer

def main():
    sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
    print(solution(sizes))

if __name__ == "__main__":
    main()