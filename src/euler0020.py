
''' Project Euler 020
    ====================
'''
import eulerlib as lib

N = 100

def weirdfact(n):
    p = 1
    while n >= 2:
        p *= n
        while not p % 10:
            p //= 10
        n -= 1
    else:
        return p

def sum_digs(n):
    s = 0
    while n > 0:
        n, r = divmod(n, 10)
        s += r
    else:
        return s

@lib.answer
def main(n: int):
    return sum_digs(weirdfact(n))

if __name__ == '__main__':
    main(N)
