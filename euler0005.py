
''' Project Euler 005
    ====================
'''
import lib

def evenly_divisible(n):
    """ Returns the smallest number which is divisible by
        numbers from 1 to n.
    """
    m = 1

    while True:
        for i in range(1, n+1):
            if m % i:
                break
        else:
            return m
        m += 1

@lib.answer
def main():
    return evenly_divisible(20)

if __name__ == '__main__':
    main()
