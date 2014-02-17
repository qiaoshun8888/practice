
def find_left_right(array, start, end, mid):
    x = array[mid]
    left = mid
    while left >= 0:
        left -= 1
        if not array[left] == x:
            break
    right = mid
    while right < len(array):
        right += 1
        if not array[right] == x:
            break
    return (left + 1, right - 1)


def revised_find_left_right(array, start, end, mid):
    x = array[mid]
    left = array[start:mid]
    right = array[mid + 1:end]

    def find_left(array, start, end, x):
        print array, start, end, x
        if end <= start:
            raise ValueError
        if start == end - 1:
            return end
        mid = start + (end - start) / 2
        if array[mid] == x:
            return find_left(array, start, mid, x)
        else:
            return find_left(array, mid, end, x)

    def find_right(array, start, end, x):
        print array, start, end, x
        if end <= start:
            raise ValueError
        if start == end - 1:
            return start
        mid = start + (end - start) / 2
        if array[mid] == x:
            return find_right(array, mid, end, x)
        else:
            return find_right(array, start, mid, x)

    return (find_left(array, start, mid, x), find_right(array, mid, end, x))


def occurance(array, x):

    def occurance_helper(array, start, end, x):
        if start > end:
            raise ValueError

        mid = start + (end - start) / 2
        if array[mid] == x:
            # some change
            # easist way
            return revised_find_left_right(array, start, end, mid)
        elif array[mid] > x:
            return occurance_helper(array, start, mid, x)
        else:
            return occurance_helper(array, mid + 1, end, x)
    return occurance_helper(array, 0, len(array) - 1, x)


def main():
    a = [1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 8, 9, 10]
    print occurance(a, 8)

if __name__ == '__main__':
    main()
