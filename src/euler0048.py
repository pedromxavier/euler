''' Project Euler 0048
    ====================
'''
import eulerlib as lib
import math

M = 10
N = 1_000

@lib.answer
def main(m: int, n: int):
    M = pow(10, m)
    return str(sum(pow(i, i, M) for i in range(1, n+1)) % M).zfill(m)

if __name__ == '__main__':
    main(M, N)
