# 2016년

def solution(a, b):
    answer = ''
    due = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sum = -1
    for i in range(0, a - 1):
        sum += date[i]
    sum += b
    answer = due[(sum % 7 + 5) % 7]
    return answer