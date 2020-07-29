## Standard Library
import math
import time
from functools import wraps, reduce
from collections import defaultdict, deque
import itertools as it

## Third-party
import numpy as np

clock = time.perf_counter

from .sieve import Sieve

INF = float('inf')
ONE_MILLION = 1_000_000
TEN_MILLION = 10_000_000
PHI = (1 + math.sqrt(5)) / 2

def iterdiv(a: int, b: int):
    k = 1
    q, r = divmod(a, b)
    yield (q, r)
    while r != 0:
        r *= pow(10, k)
        q, r = divmod(r, b)
        yield(q, r)

def ndigits(n: int):
    return math.floor(math.log10(max(abs(n), 1.0))) + 1

def ranger(*args, f=None):
    if f is None:
        if len(args) == 1:
            return [(i,) for i in range(args[0])]
        else:
            return [(i, *J) for i in range(args[-1]) for J in ranger(*args[:-1])]
    else:
        if len(args) == 1:
            return [(i,) for i in range(args[0]) if f(i)]
        else:
            return [(i, *J) for i in range(args[-1]) for J in ranger(*args[:-1], f=f) if f(i, *J)]

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

def load(fname: str):
    with open(fname, 'r') as file:
        return file.read()

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

def window(x: list, n: int):
    for i in range(len(x) - n):
        yield tuple(x[i:i+n])

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

def divisors(n: int) -> list:
    return proper_divisors(n) + [n]

def digits(n: int) -> tuple:
    stack = []
    while n:
        n, d = divmod(n, 10)
        stack.append(d)
    else:
        return tuple(reversed(stack))

def matrix(m: int, n: int, f:callable=None):
    if f is None: f = lambda i, j: None
    return [[f(i,j) for j in range(n)] for i in range(m)]

def is_prime(n: int, sieve: Sieve=None):
    """
    """
    if n <= 1:
        return False

    if sieve is None:
        if not n % 2 or not n % 3:
            return False
        for k in range(5, math.ceil(math.sqrt(n) + 1.0), 2):
            if not n % k:
                return False
        else:
            return True
    else:
        return sieve.is_prime(n)

def pandigs(n: int):
    return (sum(x * 10 ** i for i, x in enumerate(p)) for p in it.permutations(range(n, 0, -1), n))

def _new(n):
    from .template import TEMPLATE

    with open(f'euler{str(n).zfill(4)}.py', 'w') as file:
        file.write(TEMPLATE.format(n))

def nsqrt(n: int):
    k = n // 2
    while k * k > n:
        k -= 1
    while k * k < n:
        k += 1
    else:
        if (k * k == n):
            return k
        else:
            return None

def is_square(n: int):
    return nsqrt(n) is not None

def answer(callback: callable):
    @wraps(callback)
    def new_callback(*args, **kwargs):
        print('Go Euler!')
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
