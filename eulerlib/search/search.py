def binary_search(x: int, y: list):
    """ Binary search, supposes y is ordered.
    """
    i = 0
    j = len(y) - 1
    while j - i > 1:
        k = (i + j) // 2
        if y[k] > x:
            j = k
        elif y[k] < x:
            i = k
        else:
            return k
    else:
        if y[i] == x:
            return i
        elif y[j] == x:
            return j
        else:
            return None