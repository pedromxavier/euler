''' Project Euler 0039
    ====================
'''
import eulerlib as lib
import math

N = 1_000

def find(p: int):
    S = lib.defaultdict(int)
    a = 1
    while a <= p:
        b = 1
        while True:
            c = int(math.hypot(a, b))
            if a + b + c > p:
                break
            if c * c == a * a + b * b:
                S[a + b + int(c)] += 1
            b += 1
        a += 1
    return S

@lib.answer
def main(n: int):
    S = find(n)
    return lib.argmax([S[i] for i in range(n + 1)])

if __name__ == '__main__':
    main(N)
