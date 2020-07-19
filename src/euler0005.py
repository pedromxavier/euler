
''' Project Euler 005
    ====================
'''
import eulerlib as lib
import math
from functools import reduce

def evenly_divisible(n):
    """ Returns the smallest number which is divisible by
        numbers from 1 to n.
    """
    if n <= 1:
        return 1
    x = [i for i in range(n + 1)]

    primes = lib.Sieve.get_primes(n + 1)

    factor = {}

    for p in primes:
        x[p] = 1
        factor[p] = 1
        for i in range(p + p, n + 1, p):
            m = 0
            while not x[i] % p:
                x[i] //= p
                m += 1
            factor[p] = max(m, factor[p])

    return reduce(lambda a, b: a * b, [p ** factor[p] for p in factor])

@lib.answer
def main():
    return evenly_divisible(20)

##@lib.verify
def verify(x: int):
    for i in range(2, 20):
        if x % i:
            return False
    else:
        return True

if __name__ == '__main__':
    x, t = main()

    print(verify(x))
