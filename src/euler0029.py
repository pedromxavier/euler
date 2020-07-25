''' Project Euler 029
    ====================
'''
import eulerlib as lib
import math
N = 100

def calc(n: int):
    m = n + 1 ## n included in range(m)
    M = lib.matrix(m, m, lambda a, b: hash(str(pow(a, b))))
    return len(set(M[i][j] for i in range(2, m) for j in range(2, m)))

@lib.answer
def main(n: int):
    return calc(n)

if __name__ == '__main__':
    main(N)