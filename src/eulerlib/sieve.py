#Implementação em python do Crivo de Atkin
import math
import pickle
import warnings

from collections import defaultdict

class Sieve:

    LIMIT = 16777216

    @classmethod
    def get_primes(cls, limit: int):
        return cls(limit).__get_primes()

    def __iter__(self):
        return iter(self.primes)

    def __init__(self, limit: int):
        if not limit < self.LIMIT:
            warnings.warn('Very large sieves might take a (long) while. Press Ctrl+C/X to cancel operation.')

        self.limit = limit
        self.primes = []	
        self.sieve = [False]*(self.limit+1)

        self.update = False

    def flip(self, prime):
        try:
            self.sieve[prime] = not self.sieve[prime]
        except KeyError:
            pass

    def invalidate(self, prime):
        try:
            if self.sieve[prime]:
                self.sieve[prime] = False
        except KeyError:
            pass			


    def is_prime(self, prime):
        try:
            return self.sieve[prime]
        except KeyError:
            return False

    def __start(self, n: int):
        if not n % 2:
            return max(n - 1, 5)
        else:
            return max(n, 5)

    @classmethod
    def pseudo_primes(self, start: int, stop: int) -> iter:
        """ primes in 30 n ± 1, 30 n ± 7, 30 n ± 11, 30 n ± 13
        """
        for i in (2, 3, 5, 7, 11, 13):
            if i < stop:
                if i >= start:
                    yield i
            else:
                return
        j = 19
        while True:
            if j < stop:
                if i >= start:
                    yield j
                j += 4
            else:
                return
            if j < stop:
                if i >= start:
                    yield j
                j += 2
            else:
                return

        


    def __run_sieve(self, start: int=0):			
        test_limit = math.ceil(math.sqrt(self.limit))

        start = self.__start(start)

        for i in range(start - 5, test_limit):
            for j in range(start - 5, test_limit):
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

        for i in range(start, test_limit, 2):			
            if self.is_prime(i):
                k = i * i
                for j in range(k, self.limit+1, k):
                    self.invalidate(j)
                            
    def __get_primes(self):
        if not self.update:
            self.__run_sieve()
        
        return [2, 3] + [x for x in range(5, len(self.sieve), 2) if self.is_prime(x)]