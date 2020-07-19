## Standard Library
import math
import time
from functools import wraps, reduce
from collections import defaultdict

## Third-party
import numpy as np

clock = time.perf_counter

from .sieve import Sieve

INF = float('inf')

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

def factor(n, primes=None):
    res = defaultdict(int)
    
    if primes is None:
        primes = Sieve.get_primes(n // 2)

    for p in primes:
        while not n % p:
            n //= p
            res[p] += 1
    return res

def ndivisors(n, primes=None):
    return product((a + 1 for a in factor(n, primes=primes).values()))

def _new(n):
    from .template import TEMPLATE

    with open(f'euler{str(n).zfill(4)}.py', 'w') as file:
        file.write(TEMPLATE.format(n))

def answer(callback):
    @wraps(callback)
    def new_callback(*args, **kwargs):
        T = clock()
        ans = callback(*args, **kwargs)
        T = clock() - T
        print(f"Answer: {ans}")
        print(f"Time Elsapsed: {T:.03f}s")
        return ans, T
    return new_callback

def verify(callback):
    @wraps(callback)
    def new_callback():
        ...
    return new_callback
