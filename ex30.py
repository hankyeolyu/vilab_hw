# 최대공약수와 최소공배수

def gcd(n, m):
    if n < m:
        n, m = m, n
    if m == 0:
        return n
    if n % m == 0:
        return m
    else:
        return gcd(m, n % m)
def lcm(n, m):
    return n * m / gcd(n, m)
def solution(n, m):
    answer = []
    answer.append(gcd(n,m))
    answer.append(int(lcm(n,m)))
    return answer

def main():
    n = int(input())
    m = int(input())
    print(solution(n,m))

if __name__ == "__main__":
    main()