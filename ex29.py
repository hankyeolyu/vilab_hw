# 직사각형 별찍기

def main():
    a, b = map(int, input().strip().split(' '))
    for i in range(b):
        for j in range(a):
            print('*', end = '')
        print('\n', end = '')
        

if __name__ == "__main__":
    main()