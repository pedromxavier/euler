""" Project Euler 026
    ====================
"""
import eulerlib as lib

N = 1_000

def get_pattern_size(i: int):
    div = lib.iterdiv(1, i)
    q, r = next(div)
    while q == 0:
        q, r = next(div)
    else:
        s = [(q, r)]

    for q, r in div:
        s.append((q, r))
        k = len(s)
        m = k % 2
        l = k // 2
        j = m
        while l > 0:
            if s[j:j+l] == s[j+l:j+l+l]:
                return l
            else:
                j += 2
                l -= 1
    else: ## no repeating pattern
        return 0
    
def find(n: int):
    m = 0
    j = 0
    for i in range(2, n):
        k = get_pattern_size(i)
        if k > m:
            m = k
            j = i
    return j

@lib.answer
def main(n: int):
    return find(n)

if __name__ == '__main__':
    main(N)
