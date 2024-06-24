# 소수 찾기

def is_prime_number(n):
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True

def solution(n):
    answer = 0
    for i in range(2, n + 1):
        if is_prime_number(i):
            answer += 1
    return answer