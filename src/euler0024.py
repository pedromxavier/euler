
''' Project Euler 024
    ====================
'''
import eulerlib as lib

ONE_MILLION = 1_000_000
M = 10

def permute(m: int, n: int):
    n = n - 1
    x = list(range(m))
    s = [] ## stack
    k = lib.fat(m)
    n %= k
    while m > 0:
        k //= m
        i, n = divmod(n, k)
        s.append(x[i])
        x.pop(i)
        m -= 1
    return s

@lib.answer
def main(m: int, n: int):
    return ''.join(str(x) for x in permute(m, n))

if __name__ == '__main__':
    main(M, ONE_MILLION)
