
''' Project Euler 019
    ====================
'''
import eulerlib as lib
import datetime as dt

N = 0

START = dt.date(1901, 1, 1)
END = dt.date(2000, 12, 31)

def count(start: dt.date, end: dt.date):
    day = dt.timedelta(days=1)
    week = dt.timedelta(days=7)

    while start.isoweekday() != 7:
        start += day

    sundays = 0

    while start <= end:
        sundays += int(start.day == 1)
        start += week
    
    return sundays


@lib.answer
def main(start: dt.date, end: dt.date):
    return count(start, end)

if __name__ == '__main__':
    main(START, END)
