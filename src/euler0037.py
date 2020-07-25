''' Project Euler 0037
    ====================
'''
import eulerlib as lib
import math

from time import sleep

N = 11

def p(k: int):
    return lib.is_prime(k, sieve=None)

def find(n: int):
    ## final answer
    S = set()

    ## all left-sided truncatable primes
    L = set()
    LI= {1, 2, 3, 4, 5, 6, 7, 8, 9}
    LQ= lib.deque([3, 7])

    ## all right-sided truncatable primes
    R = set()
    RJ= {1, 3, 7, 9}
    RQ= lib.deque([2, 3, 5, 7])

    while len(S) < n:
        if len(LQ) == 0 and len(RQ) == 0:
            raise RuntimeError("Algorithm Failed bro.")

        if len(LQ) > 0:
            l = LQ.popleft()
            for i in LI:
                k = int(f"{i}{l}")
                if p(k):
                    L.add(k)
                    if k in R: S.add(k)
                    LQ.append(k)

        if len(RQ) > 0:
            r = RQ.popleft()
            for j in RJ:
                k = int(f"{r}{j}")
                if p(k):
                    R.add(k)
                    if k in L: S.add(k)
                    RQ.append(k)
    else:
        return S

@lib.answer
def main(n: int):
    return sum(find(n))

if __name__ == '__main__':
    main(N)
