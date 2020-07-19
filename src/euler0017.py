
''' Project Euler 017
    ====================
'''
import eulerlib as lib

ONE_THOUSAND = 1_000

## split into classes
a = [
    None, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
    'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
]

b = [
    None, None, 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
]

c = [
    'hundred', 'thousand'
]

A = {i: a[i] for i in range(1, 20)}
B = {i: b[i] for i in range(2, 10)}
C = {
    100: c[0],
    1_000: c[1]
    }

AND = "and"

def name(n):
    if 1 <= n <= 19:
        return A[n]
    elif 20 <= n <= 99:
        x, y = divmod(n, 10)
        return B[x] + name(y)
    elif 100 <= n <= 999:
        x, y = divmod(n, 100)
        return name(x) + C[100] + ((AND + name(y)) if (y > 0) else '')
    elif 1_000 <= n <= 999_999:
        x, y = divmod(n, 1_000)
        return name(x) + C[1_000] + name(y)
    else:
        return ''

def sum_all(n):
    k = 0
    for i in range(1, n + 1):
        s = name(i)
        m = len(s)
        print(s, m)
        k += m
    return k

@lib.answer
def main(n):
    return sum_all(n)

if __name__ == '__main__':
    main(ONE_THOUSAND)
