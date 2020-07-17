
''' Project Euler 005
    ====================
'''
import eulerlib as lib

def evenly_divisible(n):
    """ Returns the smallest number which is divisible by
        numbers from 1 to n.
    """
    x = lib.factor(n)

@lib.answer
def main():
    return evenly_divisible(17)

if __name__ == '__main__':
    main()
