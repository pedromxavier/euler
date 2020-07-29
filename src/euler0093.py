''' Project Euler 0093
    ====================
'''
import eulerlib as lib
import math

from itertools import permutations as perm

def decor(f):
    def g(a, b):
        if a is None:
            return b
        if b is None:
            return a
        else:
            return f(a, b)
    return g

@decor
def add(a, b):
    return a + b

@decor
def sub(a, b):
    return a - b

@decor
def div(a, b):
    return (a / b) if (b != 0) else None

@decor
def mul(a, b):
    return a * b

def ifint(x: float):
    if x is None or (x - int(x)) != 0:
        return None
    else:
        return int(x)

funcs = (add, mul, div, sub)

func_groups = [(f, g, h) for f in funcs for g in funcs for h in funcs]

trees = (
    [(lambda a, b, c, d, f=f, g=g, h=h: f(g(a, b), h(c, d))) for (f,g,h) in func_groups] + 
    [(lambda a, b, c, d, f=f, g=g, h=h: f(g(h(a, b), c), d)) for (f,g,h) in func_groups]
)

def calc(a, b, c, d):
    return {ifint(tree(x, y, z, w)) for tree in trees for (x, y, z, w) in perm((a, b, c, d), 4)} - {None}

def find():
    m = 0
    S = None

    for a in range(9):
        for b in range(a+1, 9):
            for c in range(b+1, 9):
                for d in range(c+1, 9):
                    A = calc(a, b, c, d)
                    if len(A) < m:
                        continue
                    for n in range(1, len(A)):
                        if n not in A:
                            break
                    if n > m:
                        m = n
                        S = (a, b, c, d)
    return S

@lib.answer
def main():
    return find()

if __name__ == '__main__':
    main()
