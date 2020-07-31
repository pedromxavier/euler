''' Project Euler 0046
    ====================
'''
import eulerlib as lib
import math

N = 33

def f(k: int):
    return 2 * k * k

def is_prime(n: int):
    try:
        return is_prime.cache[n]
    except KeyError:
        p = lib.is_prime(n)
        is_prime.cache[n] = p
        return p

is_prime.cache = {}

def find(n):
    while True:
        n+= 2
        if lib.is_prime(n):
            continue
        else:
            k = 1
            m = 2
            while m < n:
                if is_prime(n - m):
                    break
                else:
                    k+= 1
                    m = f(k)
            else:
                return n

@lib.answer
def main(n: int):
    return find(n)

if __name__ == '__main__':
    main(N)
