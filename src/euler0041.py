''' Project Euler 0041
    ====================
'''
import eulerlib as lib
import math

from itertools import permutations

N = 9

def find(n: int):
    if n < 4:
        return None
    elif n < 7:
        n = 4
    else:
        n = 7

    return {x for x in lib.pandigs(n) if (x % 3 in {1, 3, 7}) and lib.is_prime(x)}    

@lib.answer
def main(n: int):
    return max(find(n))

if __name__ == '__main__':
    main(N)
