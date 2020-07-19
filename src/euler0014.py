
''' Project Euler 014
    ====================
'''
import eulerlib as lib
from collections import deque, defaultdict

ONE_MILLION = 1_000_000

def f(n):
    if not n % 2:
        return n // 2
    else:
        return 3 * n + 1

def fill(n):
    assert n >= 3
    x = [None] * n
    i = 1
    k = 0
    while i < n:
        x[i] = k
        k += 1
        i *= 2
    X = defaultdict(lambda: None)

    for i in range(n-1, 1, -1):
        if x[i] is not None: continue
        y = None
        j = i
        s = [] ## stack
        while y is None:
            s.append(j)
            j = f(j)
            if j >= len(x):
                y = X[j]
            else:
                y = x[j]
            
        k = 0 ## offset
        while s:
            i = s.pop()
            if i >= len(x):
                if j >= len(x):
                    X[i] = X[j] + k
                else:
                    X[i] = x[j] + k
            else:
                if j >= len(x):
                    x[i] = X[j] + k
                else:
                    x[i] = x[j] + k
            k += 1
    return x

def find(n):
    return lib.argmax(fill(n))

@lib.answer
def main(n):
    return find(n)

if __name__ == '__main__':
    main(ONE_MILLION)
