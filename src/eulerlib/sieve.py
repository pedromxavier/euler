#Implementação em python do Crivo de Atkin
import math
import pickle
import warnings

from collections import defaultdict
from array import array

## 10 seconds

class Sieve:

    LIMIT = 16777216 #

    FACTOR = (1.0 + math.sqrt(5)) / 2 # golden ratio

    @classmethod
    def get_primes(cls, limit: int):
        return cls(limit).primes

    def __iter__(self):
        i = 0
        while True:
            if i < len(self.primes):
                yield self.primes[i]
                i += 1
            else:
                self.grow(self.FACTOR)

    def __init__(self, limit: int):
        if not limit < self.LIMIT:
            warnings.warn('Very large sieves might take a (long) while. Press Ctrl+C/X to cancel operation.')

        self.start = 0
        self.limit = max(1_000, limit)

        self.primes = []
        self.sieves = array('b', [0] * (self.limit + 1))

        self.__run_sieve()

    def flip(self, p: int):
        try:
            self.sieves[p] = not self.sieves[p]
        except KeyError:
            pass

    def invalidate(self, p: int):
        try:
            if self.sieves[p]:
                self.sieves[p] = False
        except KeyError:
            pass

    def is_prime(self, p: int):
        if p < self.limit:
            return bool(self.sieves[p])
        else:
            self.grow(self.FACTOR)
            return self.is_prime(p)
    
    def __contains__(self, p: int):
        try:
            return bool(self.sieves[p])
        except KeyError:
            return False

    @classmethod
    def prange(self, start: int, stop: int) -> iter:
        """ prime candidates in {2, 3, 6 n ± 1 : n = 1, 2, ... }
        """
        n = start // 6

        if n <= 0:
            yield 2
            yield 3
            n = 1

        k = 6 * n

        while k - 1 <= stop:
            if start <= k - 1 <= stop:
                yield k - 1
            if start <= k + 1 <= stop:
                yield k + 1
            k += 6

    def grow(self, factor: float):
        self.limit = int(self.limit * factor)
        self.sieves.extend([0] * (self.limit + 1 - len(self.sieves)))
        self.__run_sieve()

    def __test(self, i, j):
        # n = 4*i^2 + j^2
        n = 4*i*i + j*j
        if n <= self.limit and (n % 12 == 1 or n % 12 == 5):				
            self.flip(n)

        # n = 3*i^2 + j^2
        n = 3*i*i + j*j
        if n <= self.limit and n % 12 == 7:				
            self.flip(n)				

        # n = 3*i^2 - j^2
        n = 3*i*i - j*j
        if n <= self.limit and i > j and n % 12 == 11:					
            self.flip(n)

    def __run_sieve(self):			
        test_limit = math.ceil(math.sqrt(self.limit))

        for i in range(self.start):
            for j in range(self.start, test_limit):
                self.__test(i, j)

        for i in range(self.start, test_limit):
            for j in range(test_limit):
                self.__test(i, j)

        for i in self.prange(5, test_limit):			
            if self.is_prime(i):
                k = i * i
                for j in range(k, self.limit + 1, k):
                    self.invalidate(j)

        self.primes.extend([x for x in self.prange(len(self.primes), self.limit + 1) if i in self])
        self.start = test_limit

    def primes_until(self, n: int):
        for p in self:
            if p > n:
                break
            else:
                yield p