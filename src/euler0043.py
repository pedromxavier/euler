''' Project Euler 0043
    ====================
'''
import eulerlib as lib
import math

N = 9

def check(di: int, dj: int, dk: int, k: int):
    return not ((100 * di + 10 * dj + dk) % k)

def chec3(di: int, dj: int, dk: int):
    return not ((di + dj + dk) % 3)

def count(n: int):
    S1 = {s for s in range(0, n + 1, 1)}
    S2 = {s for s in range(0, n + 1, 2)}
    S5 = {s for s in range(0, n + 1, 5)}

    s = 0

    for d6 in S5:
        R6 = {d6}
        for d4 in (S2 - R6):
            R4 = {*R6, d4}
            for d3 in (S1 - R4):
                R3 = {*R4, d3}
                for d5 in (S1 - R3):
                    if not chec3(d3, d4, d5): continue
                    R5 = {*R3, d5}
                    for d7 in (S1 - R5):
                        if not check(d5, d6, d7, 7): continue
                        R7 = {*R5, d7}
                        for d8 in (S1 - R7):
                            if not check(d6, d7, d8, 11): continue
                            R8 = {*R7, d8}
                            for d9 in (S1 - R8):
                                if not check(d7, d8, d9, 13): continue
                                R9 = {*R8, d9}
                                for d10 in (S1 - R9):
                                    if not check(d8, d9, d10, 17): continue
                                    R10 = {*R9, d10}
                                    for d1 in (S1 - R10):
                                        R1 = {*R10, d1}
                                        for d2 in (S1 - R1):
                                            d = (d1, d2, d3, d4, d5, d6, d7, d8, d9, d10)
                                            r = lib.from_digits(d)
                                            s+= r
    return s


@lib.answer
def main(n: int):
    return count(n)

if __name__ == '__main__':
    main(N)
