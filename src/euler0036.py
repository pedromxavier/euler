''' Project Euler 0036
    ====================
'''
import eulerlib as lib
import math

N = lib.ONE_MILLION

def dual_palindrome(n: int):
    b10 = str(n)
    b2 = bin(n)[2:]
    return b10 == b10[::-1] and b2 == b2[::-1]

def calc(n: int):
    s = 0
    for k in range(1, n):
        if dual_palindrome(k):
            s += k
    return s

@lib.answer
def main(n: int):
    return calc(n)

if __name__ == '__main__':
    main(N)
