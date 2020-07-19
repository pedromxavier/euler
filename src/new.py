if __name__ == '__main__':
    from eulerlib import _new
    from sys import argv

    if len(argv) == 1:
        print("""
Usage:
new_euler m ... n
""")
    else:
        for n in map(int, argv[1:]):
            _new(n)

else:
    raise ImportError("You can't import this file")
