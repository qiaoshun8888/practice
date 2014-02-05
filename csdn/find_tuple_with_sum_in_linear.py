"""
# 14

I saw the answer ... before I solve it
My origin opinion is get the diff, then try solve it by the diff
[0, 1, 2, 3, 4, 4], I think I am confused totally
"""


def find(array, x):
    l = 0
    r = len(array) - 1

    while l < r:
        if array[l] + array[r] == x:
            return array[l], array[r]
        elif array[l] + array[r] > x:
            r -= 1
        elif array[l] + array[r] < x:
            l += 1
    return 'error'

if __name__ == '__main__':
    print find([1, 2, 4, 7, 11, 15], 15)
