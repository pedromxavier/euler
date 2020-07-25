''' Project Euler 0038
    ====================
'''
import eulerlib as lib
import math

def pandig(n: int, digits: tuple):
    S = [True] + [False] * n
    for k in digits:
        if S[k]:
            return False
        else:
            S[k] = True
    else:
        return all(S)

def calc(x: int, n: int):
    return sum(map(lib.digits, ((x * y) for y in range(1, n + 1))), tuple())

def find():
    n = 2
    while n <= 9:
        x = 10 ** (n // 9)
        while n * lib.ndigits(x) <= 9:
            digits = calc(x, n)
            if len(digits) != 9:
                x += 1
                continue
            if pandig(9, digits):
                yield int("".join(map(str, digits)))
            x += 1
        n += 1
            
@lib.answer
def main():
    S = list(find())
    return max(S)

if __name__ == '__main__':
    main()
