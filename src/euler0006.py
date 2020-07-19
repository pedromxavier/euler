
''' Project Euler 006
    ====================
'''
import eulerlib as lib

def sum_2(n: int):
    return ((n + 1) ** 3 - (n + 1)) // 3 - (n * (n + 1)) // 2

def sum_1(n: int):
    return (n * (n + 1)) // 2

@lib.answer
def main(n):
    a = sum_1(n)
    b = sum_2(n)
    return a * a - b

if __name__ == '__main__':
    main(100)
