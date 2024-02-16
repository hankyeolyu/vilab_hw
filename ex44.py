# 두 개 뽑아서 더하기

def solution(numbers):
    answer = []
    
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    
    answer = list(set(answer))
    answer.sort()
    
    return answer

def main():
    numbers = [2,1,3,4,1]
    print(solution(numbers))

if __name__ == '__main__':
    main()