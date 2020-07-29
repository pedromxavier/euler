''' Project Euler 0042
    ====================
'''
import eulerlib as lib
import math

WORDS = eval(f"[{lib.load('euler0042.txt')}]")

def t(n: int):
    return (n * (n + 1)) // 2

def gematria(word: str):
    A = ord('A') - 1 
    return sum((ord(c) - A) for c in word)

def is_triangle(n: int):
    k = 1 + 8 * n
    r = lib.nsqrt(k)
    if r is None:
        return False
    else:
        return not ((r - 1) % 2)

def count(words: list):
    return sum(is_triangle(gematria(word)) for word in words)

@lib.answer
def main(words: list):
    return count(words)

if __name__ == '__main__':
    main(WORDS)