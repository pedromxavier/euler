
''' Project Euler 030
    ====================
'''
import eulerlib as lib
import math

K = 5

def f(n: int, k: int):
    return n == sum(pow(d, k) for d in lib.digits(n))

def u(n: int, k: int):
    """ upper bound"""
    return n / (math.log10(n) + 1) <= pow(9, k)

def find(k:int):
    n = 2
    s = 0
    while u(n, k):
        if f(n, k):
            s += n
        n += 1
    return s

@lib.answer
def main(k: int):
    return find(k)

if __name__ == '__main__':
    main(K)
