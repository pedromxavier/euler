''' Project Euler 0079
    ====================
'''
import eulerlib as lib
import math

KEYLOG = [tuple(int(x) for x in line) for line in lib.load('euler0079.txt').split('\n')]

def adj_mtx(keylog: list) -> (set, set):
    mtx = set()
    idx = set()
    for code in keylog:
        m = len(code)
        for i in range(m):
            x = code[i]
            idx.add(x)
            for j in range(i+1, m):
                y = code[j]
                mtx.add((x, y))
                idx.add(y)
    return mtx, idx

def ideg(mtx: set, idx: set, j: int):
    'in-degree'
    return sum((i, j) in mtx for i in idx)

def odeg(mtx: set, idx:set, i: int):
    'out-degree'
    return sum((i, j) in mtx for j in idx)

def sort(mtx: set, idx: set):
    pos = sorted([x for x in idx], key=lambda i: ideg(mtx, idx, i))
    return pos

def find(keylog: list):
    mtx, idx = adj_mtx(keylog)

    pos = [set() for i in range(len(idx))]

    pos[0].update(idx)

    while not all(len(s) == 1 for s in pos):
        k = 1
        while k < len(pos):
            mov = {j for i in pos[k-1] for j in (pos[k-1] - {i}) if (i, j) in mtx}

            pos[k-1].difference_update(mov)
            pos[k].update(mov)

            k += 1
    else:
        return pos

@lib.answer
def main(keylog: list):
    return find(keylog)

if __name__ == '__main__':
    main(KEYLOG)
