
''' Project Euler 050
    ====================
'''
import eulerlib as lib

def find(n):
    primes = [p for p in range(n) if lib.is_prime(p)]
    m = 0
    r = 0
    for i in range(len(primes)):
        k = 0
        s = 0
        for j in range(i, len(primes)):
            s+= primes[j]
            if s > n:
                break
            if lib.is_prime(s):
                if k > m:
                    m = k
                    r = s
            k += 1
    return r

@lib.answer
def main(n: int):
    return find(n)

if __name__ == '__main__':
    main(lib.ONE_MILLION)
