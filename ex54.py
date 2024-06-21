import math
import itertools

def is_prime_number(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0

    for i in itertools.combinations(nums, 3):
        if is_prime_number(sum(i)):
            answer += 1

    return answer
