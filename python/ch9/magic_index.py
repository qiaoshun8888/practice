"""
A magic index in an array A[0, ..., n-1]
An index such that A[i] = if __name__ == '__main__':
Given a sorted array, write a method to find a magic index.
"""


def find_magic(array):
    i = 0
    while i < len(array):
        if array[i] == i:
            yield i
        elif array[i] > i:
            i = array[i] - 1  # not distinct
            # if it's distinct than break
        i += 1

if __name__ == '__main__':
    a = [1, 1, 2, 3, 4, 5, 8, 9, 10, 11]
    for i in find_magic(a):
        print i
