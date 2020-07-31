''' Project Euler 0097
    ====================
'''
import eulerlib as lib
import math

## y = a * 2 ** b + 1

N = 10

A = 28433
B = 7830457

def calc(a: int, b: int, n: int):
    m = pow(10, n)
    x = a * pow(2, b, m) + 1
    return x % m

@lib.answer
def main(a:int, b: int, n: int):
    return calc(a, b, n)

if __name__ == '__main__':
    main(A, B, N)
