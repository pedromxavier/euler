''' Project Euler 0065
    ====================
'''
import eulerlib as lib
import math

N = 100

def f(k: int):
    if k <= 0:
        return 0
    if k == 1:
        return 2
    elif not k % 3:
        return 2 * (k // 3)
    else:
        return 1

def e(n: int):
    x = [f(k) for k in range(1, n + 1)]
    ## e = p / q

    p = 1
    q = x.pop()
    while x:
        p, q = q, q * x.pop() + p
    else:
        return (p, q)

@lib.answer
def main(n: int):
    return sum(lib.digits(e(n)[1]))

if __name__ == '__main__':
    main(N)
