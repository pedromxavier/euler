
''' Project Euler 032
    ====================
'''
import eulerlib as lib
from itertools import permutations

def unique(digits: tuple):
    n = len(digits)
    for i in range(n):
        for j in range(i + 1, n):
            if digits[i] == digits[j]:
                return False
    else:
        return True


def find() -> set:
    rng = set(range(1, 10))
    res = set()
    for a in range(1, 100):
        da = lib.digits(a)
        if not unique(da): continue
        for b in range(100, 10_000):
            db = da + lib.digits(b)
            if not unique(db): continue
            c = a * b
            dc = db + lib.digits(c)
            if unique(dc) and set(dc) == rng:
                res.add(c)
                print(f"{a} x {b} = {c}")
    return res

@lib.answer
def main():
    return sum(find())

if __name__ == '__main__':
    main()
