''' Project Euler 0052
    ====================
'''
import eulerlib as lib
import math

N = 6

def pattern(n: int):
    p = {}
    for d in lib.digits(n):
        try:
            p[d] += 1
        except KeyError:
            p[d] = 1
    else:
        return p

def all_equal(items: list):
    x = items[0]
    for i in range(1, len(items)):
        y = items[i]
        if x != y:
            return False
        else:
            x = y
    else:
        return True

def find(n: int):
    x = 1
    while True:
        if all_equal([pattern(x * k) for k in range(1, n + 1)]):
            return x
        else:
            x = x + 1

@lib.answer
def main(n: int):
    return find(n)

if __name__ == '__main__':
    main(N)
