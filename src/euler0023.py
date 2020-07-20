
''' Project Euler 023
    ====================
'''
import eulerlib as lib

N = 28123

def d(n: int):
    return sum(lib.proper_divisors(n))

def find(n: int):
    ## abundant numbers
    x = [None] + [(d(i) > i) for i in range(1, n + 1)]
    ## numbers composed by sum of abundants
    y = [None] + [False] * n

    i = 1
    while i <= n:
        if not x[i]:
            i += 1
            continue
        j = i
        while j + i <= n:
            if not x[j]:
                j += 1
                continue
            y[i + j] = True
            j += 1
        i += 1
    return y

@lib.answer
def main(n: int):
    y = find(n)
    return sum([i for i in range(1, n + 1) if not y[i]])

if __name__ == '__main__':
    main(N)
