
''' Project Euler 025
    ====================
'''
import eulerlib as lib
import math

DIGITS = 1_000

def find(d: int):
    k = math.floor(math.log(math.sqrt(5), lib.PHI) + d * math.log(10, lib.PHI))
    i, j = lib.fib(k)
    while lib.digits(i) >= 1_000:
        i, j = j - i, i
        k -= 1
    return k + 1

@lib.answer
def main(d: int):
    return find(d)

if __name__ == '__main__':
    main(DIGITS)
