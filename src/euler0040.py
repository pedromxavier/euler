''' Project Euler 0040
    ====================
'''
import eulerlib as lib
import math

N = 7

def D(n: int):
    k = 1
    d = 0
    m = 0
    
    while k + d <= n:
        k += d
        d = (m + 1) * 9 * pow(10, m)
        m += 1
    else:
        q, r = divmod(n - k, m)
        return lib.digits(pow(10, m - 1) + q)[r]

@lib.answer
def main(n: int):
    digits = [D(10 ** i) for i in range(n)]
    print(digits)
    return lib.product(digits)

if __name__ == '__main__':
    main(N)