
''' Project Euler 050
    ====================
'''
import eulerlib as lib
from collections import deque

ONE_MILLION = 1_000_000

def find(n):
    primes = lib.Sieve.get_primes(n)

    q = deque([])
    m = len(primes)
    s = 0
    for p in reversed(primes):
        i = 0
        while i < m:
            while s < p:
                

            i += 1



@lib.answer
def main(n: int):
    ...

if __name__ == '__main__':
    main(ONE_MILLION)
