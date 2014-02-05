'''
# 9
'''


def is_bst_post_order(array):
    '''
    last element is root
    partition with it, recursively judge
    '''
    if len(array) < 2:
        return True

    root = array[-1]
    sp = -2
    for k, i in enumerate(array[:-1]):
        if i > root:
            sp = k - 1
            break

    if not is_bst_post_order(array[:sp + 1]):
        return False
    if not is_bst_post_order(array[sp + 1:-1]):
        return False

    if root < array[sp]:
        return False
    if root > array[-2]:
        return False
    return True


def maim():
    test = [5, 7, 6, 9, 11, 10, 8]
    print is_bst_post_order(test)


if __name__ == '__main__':
    maim()
