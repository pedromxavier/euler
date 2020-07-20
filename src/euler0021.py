
''' Project Euler 021
    ====================
'''
import eulerlib as lib

N = 10_000

def d(n: int):
    return sum(lib.proper_divisors(n))

def find(n: int):
    x = [False] * (n + 1)
    for i in range(1, n):
        if x[i]:
            continue
        else:
            j = d(i)
            if d(j) == i and i != j: ## are amicable
                x[i] = x[j] = True
    return x

@lib.answer
def main(n: int):
    x = find(n)
    return sum(i for i in range(1, n + 1) if x[i])

if __name__ == '__main__':
    main(N)
