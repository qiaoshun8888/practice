
def find_start(l, start, end):
    if end - start <= 1:
        return start
    mid = (end - start) / 2 + start
    if l[mid] > l[start]:
        return find_start(l, mid + 1, end)
    else:
        return find_start(l, start, mid)


def find(l, x):
    offset = find_start(l, 0, len(l) - 1)

    def _find(l, x, start, end):
        mid = start + (end - start) / 2
        _mid = mid + offset
        _start = start + offset
        _end = end + offset
        if l[_mid] > x:
            return _find(l, x, start, mid)
        elif l[_mid] == x:
            return _mid
        else:
            return _find(l, x, mid + 1, end)
    return _find(l, x, 0, len(l) - 1)

if __name__ == '__main__':
    print find([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5)
