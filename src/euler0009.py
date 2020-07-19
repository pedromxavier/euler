
''' Project Euler 009
    ====================
'''
import eulerlib as lib

def find_triplet():
    a = 1
    while a <= 333:
        b = a + 1
        while b <= 666:
            c = 1000 - a - b
            if a * a + b * b == c * c:
                return a, b, c
            b += 1
        a += 1
    return None

@lib.answer
def main():
    a, b, c = find_triplet()
    print(f"The triplet: ({a}, {b}, {c})")
    return a * b * c

if __name__ == '__main__':
    main()
