# K번째 수

def solution(array, commands):
    answer = []
    tmp = []
    
    for i in range(len(commands)):
        tmp = array[commands[i][0] - 1 : commands[i][1]]
        tmp.sort()
        ind = commands[i][2]
        answer.append(tmp[ind - 1])
    
    return answer

def main():
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    print(solution(array, commands))

if __name__ == '__main__':
    main()