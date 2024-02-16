# 비밀지도

import numpy as np

def dig2bin(n, num):
    result = []
    
    while len(result) < n:
        result.append(num % 2)
        num = num // 2
    
    result.reverse()
    
    return result

def solution(n, arr1, arr2):
    answer = []
    
    tmp_1 = []
    
    for i in range(0, n):
        tmp_1.append(dig2bin(n, arr1[i]))
    
    tmp_2 = []
    
    for j in range(0, n):
        tmp_2.append(dig2bin(n, arr2[j]))
    
    for i in range(0, n):
        for j in range(0, n):
            tmp_1[i][j] = tmp_1[i][j] + tmp_2[i][j]
    
    
    for i in range(0, n):
        row = []
        for j in range(0, n):
            if tmp_1[i][j] != 0:
                row.append('#')
            else:
                row.append(' ')
        row = ''.join(row)
        answer.append(row)
    
    return answer

def main():
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    print(solution(n,arr1,arr2))

if __name__ == '__main__':
    main()