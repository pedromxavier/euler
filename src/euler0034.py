''' Project Euler 0034
    ====================
'''
import eulerlib as lib
import math

M = math.factorial(9)

def u(n: int):
    'upper bound'
    return (n / math.log10(n)) <= M

def find():
    n = 10
    s = set()
    while u(n):
        if n == sum(math.factorial(d) for d in lib.digits(n)):
            s.add(n)
        n += 1
    else:
        return s

@lib.answer
def main():
    return sum(find())

if __name__ == '__main__':
    main()
