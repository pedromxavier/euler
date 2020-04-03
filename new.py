if __name__ == '__main__':
    from lib import _new
    from sys import argv

    if len(argv) == 0:
        print("""
Usage:
new_euler m ... n
""")
    else:
        for n in map(int, argv):
            _new(n)

else:
    raise ImportError("You can't import this file")
