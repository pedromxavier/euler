''' Project Euler 0045
    ====================
'''
import eulerlib as lib
import math

N = 40755

def is_triangle(n: int):
    k = 1 + 8 * n
    r = lib.nsqrt(k)
    if r is None:
        return False
    else:
        return not ((-1 + r) % 2)

def is_pentagon(n: int):
    k = 1 + 24 * n
    r = lib.nsqrt(k)
    if r is None:
        return False
    else:
        return not ((1 + r) % 6)

def h(n: int):
    k = 1 + 8 * n
    r = lib.nsqrt(k)
    if r is None:
        return False
    else:
        if not ((1 + r) % 4):
            return (1 + r) // 4
        else:
            return None

def H(n: int):
    return n * (n + n - 1)

def is_both(n: int):
    return is_pentagon(n) and is_triangle(n)

def find(n: int):
    k = h(n) + 1
    n = H(k)
    while not is_both(n):
        k+= 1
        n = H(k)
    else:
        return n

@lib.answer
def main(n: int):
    return find(n)

if __name__ == '__main__':
    main(N)
