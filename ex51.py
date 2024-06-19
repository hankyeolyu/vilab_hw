# 기사단원의 무기

def measure_count(num):
    divisor = []
    for i in range(1, int(num**(1/2)) + 1):
        if num % i == 0:
            divisor.append(i)
            if i != num // i:
                divisor.append(num // i)
    return len(divisor)

def solution(number, limit, power):
    answer = 0
    msr_cnt = []
    for i in range(1, number + 1):
        msr_cnt.append(measure_count(i))
        
    for i in range(0, len(msr_cnt)):
        if msr_cnt[i] > limit:
            answer += power
        else:
            answer += msr_cnt[i]
                
    return answer