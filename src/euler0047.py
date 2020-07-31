''' Project Euler 0047
    ====================
'''
import eulerlib as lib
import math

N = 4

def factor(n, primes=None):
    return set(lib.factor(n, primes=primes).items())

def find(n: int):
    k = 1
    P = lib.Sieve.get_primes(lib.ONE_MILLION)
    while True:
        k += n
        fk = factor(k, primes=P)
        if len(fk) == n:
            U = fk
            A = True
            B = True
            i = k
            m = 1
            for j in range(1, n):
                if A:
                    a = factor(k - j, primes=P)
                    if len(a) != n or U.intersection(a):
                        A = False
                    else:
                        i = k - j
                        m+= 1
                        U.update(a)
                if B:
                    b = factor(k + j, primes=P)
                    if len(b) != n or U.intersection(b):
                        B = False
                    else:
                        m+= 1
                        U.update(b)

                if m == n:
                    return i

                if not (A or B):
                    break     

@lib.answer
def main(n: int):
    return find(n)

if __name__ == '__main__':
    main(N)
