
''' Project Euler 016
    ====================
'''
import eulerlib as lib

def find(n):
    return sum(int(c) for c in str(1 << n))

@lib.answer
def main(n):
    return find(n)

if __name__ == '__main__':
    main(1_000)
