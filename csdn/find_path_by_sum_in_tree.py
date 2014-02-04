
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs import binary_tree


def find_path(rootnode, with_sum):
    if not rootnode:
        return []

    if rootnode.data == with_sum:
        return [[rootnode]]

    res = []
    tmp = find_path(rootnode.left, with_sum)
    if tmp:
        res.extend(tmp)
    tmp = find_path(rootnode.right, with_sum)
    if tmp:
        res.extend(tmp)
    find_path(rootnode.right, with_sum)
    rest = with_sum - rootnode.data
    tmp = find_path(rootnode.left, rest)
    if tmp:
        tmp = [[rootnode].extend(i) for i in tmp]
        if tmp:
            res.extend(tmp)
    tmp = find_path(rootnode.right, rest)
    if tmp:
        tmp = [[rootnode].extend(i) for i in tmp]
        if tmp:
            res.extend(tmp)
    return res


def main():
    rootnode = binary_tree.array2tree([10, 5, 12, 4, 7])
    print find_path(rootnode, 22)

if __name__ == '__main__':
    main()
