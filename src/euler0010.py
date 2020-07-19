
''' Project Euler 010
    ====================
'''
import eulerlib as lib

def sum_primes(n):
    return sum(lib.Sieve.get_primes(n))

@lib.answer
def main(n):
    return sum_primes(n)

if __name__ == '__main__':
    main(2_000_000)
