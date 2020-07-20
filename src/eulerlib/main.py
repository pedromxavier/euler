## Standard Library
import math
import time
from functools import wraps, reduce
from collections import defaultdict
from itertools import combinations

## Third-party
import numpy as np

clock = time.perf_counter

from .sieve import Sieve

INF = float('inf')
ONE_MILLION = 1_000_000
TEN_MILLION = 10_000_000
PHI = (1 + math.sqrt(5)) / 2

def digits(n: int):
    k = 0
    n = abs(n)
    while n > 0:
        n //= 10
        k += 1
    return max(k, 1)

def fib(n: int):
    i, j = 0, 1
    while n > 0:
        i, j = j, i + j
        n -= 1
    return i, j

def fat(n: int):
    p = 1
    while n > 1:
        p *= n
        n -= 1
    return p

def argmin(x: list):
    return min(range(len(x)), key=lambda i: x[i] if x[i] is not None else INF)

def argmax(x: list):
    return max(range(len(x)), key=lambda i: x[i] if x[i] is not None else -INF)

def product(x: list):
    return reduce(lambda a, b: a * b, x, 1)

def gcd(a, b):
    if not b:
        return a
    else:
        return gcd(b, a % b)

def factor(n, primes=None) -> dict:
    """
    """
    res = defaultdict(int)
    
    if primes is None:
        primes = Sieve.get_primes(n // 2)

    for p in primes:
        while not n % p:
            n //= p
            res[p] += 1
    return res

def ndivisors(n, primes=None) -> int:
    return product((a + 1 for a in factor(n, primes=primes).values()))

def proper_divisors(n) -> list:
    return [1] + [i for i in range(2, n // 2 + 1) if not n % i ]

def divisors(n) -> list:
    return proper_divisors(n) + [n]

def is_prime(n, sieve=None):
    """
    """
    if sieve is None or sieve.primes[-1] < n // 2:
        sieve = Sieve(n // 2)
        for p in sieve:
            if not n % p:
                return False
        else:
            return True
    else:
        return binary_search(sieve.primes, n) is not None



    

def _new(n):
    from .template import TEMPLATE

    with open(f'euler{str(n).zfill(4)}.py', 'w') as file:
        file.write(TEMPLATE.format(n))

def answer(callback: callable):
    @wraps(callback)
    def new_callback(*args, **kwargs):
        T = clock()
        ans = callback(*args, **kwargs)
        T = clock() - T
        print(f"Answer: {ans}")
        print(f"Time Elsapsed: {T:.03f}s")
        return ans, T

    def verify(callback: callable):
        @wraps(callback)
        def newest_callback(*args, **kwargs):
            ...
        return newest_callback

    setattr(new_callback, 'verify', verify)

    return new_callback



def binary_search(x: int, y: list):
    """ Binary search, supposes y is ordered.
    """
    i = 0
    j = len(y) - 1
    while j - i > 1:
        k = (i + j) // 2
        if y[k] > x:
            j = k
        elif y[k] < x:
            i = k
        else:
            return k
    else:
        if y[i] == x:
            return i
        elif y[j] == x:
            return j
        else:
            return None
