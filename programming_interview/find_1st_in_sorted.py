def find(array, x):
    def bs_helper(array, start, end, x):
        mid = start + (end - start) / 2
        if array[mid] == x:
            return start, mid
        elif array[mid] > x:
            return bs_helper(array, start, mid, x)
        elif array[mid] < x:
            return bs_helper(array, mid + 1, end, x)

    def find_left(array, start, end, x):
        mid = start + (end - start) / 2
        if start == end:
            return start
        if array[mid] == x:
            return find_left(array, start, mid, x)
        else:
            return find_left(array, mid + 1, end, x)

    start, mid = bs_helper(array, 0, len(array), x)
    return find_left(array, start, mid, x)


def main():
    a = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10,
         11, 11, 12, 13, 14, 15, 16, 16, 16, 16, 16]
    x = 5
    i = find(a, x)
    print i, a[i] == x, a[i - 1] == x

if __name__ == '__main__':
    main()
