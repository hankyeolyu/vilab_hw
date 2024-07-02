# [2020 카카오 인턴십] 키패드 누르기

def solution(numbers, hand):
    answer = ''
    l = "*"
    r = "#"
    lefts = [1,4,7,'*']
    rights = [3,6,9,'#']
    mids = [2,5,8,0]
    
    for n in numbers:
        if n in lefts:
            answer += "L"
            l = n
        elif n in rights:
            answer += "R"
            r = n
        else:
            m = mids.index(n)
            if l in lefts:
                l_dif = abs(m - lefts.index(l))
            else:
                l_dif = abs(m - mids.index(l)) - 1
            if r in rights:
                r_dif = abs(m - rights.index(r))
            else:
                r_dif = abs(m - mids.index(r)) - 1
            
            if l_dif > r_dif:
                answer += "R"
                r = n
            elif l_dif < r_dif:
                answer += "L"
                l = n
            else:
                if hand == 'right':
                    answer += "R"
                    r = n
                else:
                    answer += "L"
                    l = n
    return answer