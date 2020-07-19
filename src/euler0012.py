
''' Project Euler 012
    ====================
'''
import eulerlib as lib

def t(n):
    return (n * (n + 1)) // 2

def find(n):
    primes = lib.Sieve.get_primes(lib.math.ceil(n * lib.math.log(n)))
    m = 0
    i = 0
    while m < n:
        i += 1
        m = lib.ndivisors(t(i), primes)
    return t(i)

@lib.answer
def main(n=500):
    return find(n)

if __name__ == '__main__':
    main(500)
