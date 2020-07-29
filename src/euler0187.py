''' Project Euler 0187
    ====================
'''
import eulerlib as lib
import math
import numpy as np

N = pow(10, 8)


def count(n: int):
    m = math.ceil(math.sqrt(n))
    sieve = lib.Sieve(m)
    
    for p in sieve.primes_range(m):
        for q in sieve.primes_range(p, m):

    
@lib.answer
def main(n: int):
    return count(n)

if __name__ == '__main__':
    main(N)
