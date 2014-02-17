'''
certain level of tree
'''
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs.binary_tree import array2tree


def certain_level(root, level):
    '''
    BFS already done, so use recursive LDFS this time.
    '''
    # print root.data, level
    if level == 0:
        print root.data
    else:
        if root.left:
            certain_level(root.left, level - 1)
        if root.right:
            certain_level(root.right, level - 1)


def main():
    a = array2tree([1, 2, 3, 4, 5, 6, 7])
    certain_level(a, 2)

if __name__ == '__main__':
    main()
