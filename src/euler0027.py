''' Project Euler 027
    ====================
'''
import eulerlib as lib

N = 1000

def f(n, a, b):
    return n * (n + a) + b

def prime_length(a: int, b: int, sieve: lib.Sieve=None):
    n = 0
    while True:
        k = f(n, a, b)
        if not lib.is_prime(k, sieve):
            return n
        else:
            n += 1

def find(n: int):
    ab = 0
    a = -n + 1
    m = 0
    while a < n:
        b = -n + 1
        while b < n:
            k = prime_length(a, b)
            if k > m:
                m = k
                ab = a * b
            b += 1
        a += 1
    else:
        return ab

@lib.answer
def main(n: int):
    return find(n)

if __name__ == '__main__':
    main(N)
