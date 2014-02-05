# coding=utf-8
'''
# 5
using heap
time complexity O(n + klgn)
no extra space
'''
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs import heap


def main(k):
    test = [1, 2, 3, 4, 5, 6, 7, 8]
    h = heap.gen_minheap(test)
    res = []
    for i in range(k):
        res.append(h.pop())
    print res


if __name__ == '__main__':
    main(4)
