''' Project Euler 0044
    ====================
'''
import eulerlib as lib
import math

def P(n: int):
    return n * (3 * n - 1) // 2

def is_pentagon(n: int):
    k = 1 + 24 * n
    r = lib.nsqrt(k)
    if r is None:
        return False
    else:
        return not ((1 + r) % 6)

def find():
    k = 2
    while True:
        pk = P(k)
        j = 1
        while j < k:
            pj = P(j)
            if  is_pentagon(pk - pj) and is_pentagon(pj + pk):
                return pk - pj
            else:
                j += 1
        k += 1

@lib.answer
def main():
    return find()

if __name__ == '__main__':
    main()
