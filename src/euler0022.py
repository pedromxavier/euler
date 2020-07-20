
''' Project Euler 022
    ====================
'''
import eulerlib as lib
from string import ascii_uppercase as letters

with open('euler0022.txt') as file:
    NAMES = eval(f"[{file.read()}]")

SCORES = {c: i for i, c in enumerate(letters, 1)}

def name_score(name: str):
    return sum(SCORES[c] for c in name)

@lib.answer
def main(names: list):
    return sum(i * name_score(name) for i, name in enumerate(sorted(names), 1))

if __name__ == '__main__':
    main(NAMES)
