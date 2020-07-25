
''' Project Euler 028
    ====================
'''
import eulerlib as lib

N = 1_001

def find(n: int):
    if not n % 2: raise ValueError
    k = 1
    m = 3
    while m <= n:
        while k < m * m:
            yield k
            k += (m - 1)
        m += 2
    else:
        yield k

@lib.answer
def main(n: int):
    return sum(find(n))

if __name__ == '__main__':
    main(N)
