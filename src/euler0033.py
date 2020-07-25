''' Project Euler 032
    ====================
'''
import eulerlib as lib

N = 10

def f(a: int, b: int, c:int) -> bool:
    return (10 * a + b) * c == (10 * b + c) * a and (10 * a + b) < (10 * b + c)

def g(a: int, b: int, c:int) -> bool:
    return (10 * a + b) * c == (10 * c + b) * a and (10 * a + b) < (10 * c + b) 

def find(n: int):
    p = 1
    q = 1
    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                if f(a, b, c):
                    p *= (10 * a + b)
                    q *= (10 * b + c)
                elif g(a, b, c):
                    p *= (10 * a + b)
                    q *= (10 * c + b)
    r = lib.gcd(p, q)
    p //= r
    q //= r
    return (p, q)

@lib.answer
def main(n: int):
    p, q = find(n)
    return q

if __name__ == '__main__':
    main(N)
