''' Project Euler 0049
    ====================
'''
import eulerlib as lib
import math

N = 4

def find(n: int):
    primes = [p for p in range(1237, 9874) if lib.is_prime(p)]
    primes = [((p, set(lib.digits(p))), (q, set(lib.digits(q)))) for p in primes for q in primes if q > p]

    arithm = {}

    answer = set()

    for P, Q in primes:
        p, dp = P
        q, dq = Q
        if dp != dq:
            continue
        else:
            key = (tuple(sorted(dp)), q - p)
            
            if key in arithm:
                arithm[key].update({p, q})
            else:
                arithm[key] = {p, q}

            if len(arithm[key]) == 3:
                s = int("".join(map(str, sorted(arithm[key]))))
                answer.add(s)
    else:
        return list(answer - {148748178147})[0]

@lib.answer
def main(n: int):
    return find(n)

if __name__ == '__main__':
    main(N)
