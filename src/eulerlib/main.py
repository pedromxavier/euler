## Standard Library
import math
import time
from functools import wraps
from collections import defaultdict

## Third-party
import numpy as np

clock = time.perf_counter

def gcd(a, b):
    if not b:
        return a
    else:
        return gcd(b, a % b)

def factor(n):
    res = defaultdict(int)
    while not n % 2:
        n >>= 1
        res[2] += 1
    for i in range(3, math.ceil(math.sqrt(n)), 2):
        while not n%i:
            n //= i
            res[i] += 1
    return res

def _new(n):
    from .template import TEMPLATE

    with open(f'euler{str(n).zfill(4)}.py', 'w') as file:
        file.write(TEMPLATE.format(n))

def answer(callback):
    @wraps(callback)
    def new_callback():
        T = clock()
        ans = callback()
        T = clock() - T
        print(f"Answer: {ans}")
        print(f"Time Elsapsed: {round(T, 3)}s")
        return ans, T
    return new_callback