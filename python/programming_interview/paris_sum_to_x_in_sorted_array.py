"""
print all paris sum to x in sorted array
"""


def print_sum(array, x):
    array.sort()
    if array[-1] * 2 < x or array[0] * 2 > x:
        raise ValueError
    else:
        left = 0
        right = len(array) - 1
        while left < right:
            s = array[left] + array[right]
            if s == x:
                yield array[left], array[right]
                left += 1
                right -= 1
            elif s > x:
                right -= 1
            else:
                left += 1


def main():
    for i in print_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 5):
        print i

if __name__ == '__main__':
    main()
