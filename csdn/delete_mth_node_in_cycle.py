'''
# 18

delete m in cycle until left 1 node
'''
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs import linkedlist


def loop_delete(cycle, m):
    '''
    brutal O(n-1)
    '''
    def next(node, m):
        for i in range(m - 1):
            node = node.next
        return node

    while not cycle == cycle.next:
        next_m = next(cycle, m)
        next_m.data = next_m.next.data
        next_m.next = next_m.next.next
        cycle = next_m
    return cycle


def main(n, m):
    ll = linkedlist.array2linkedlist(range(n), True)
    ll[-1].next = ll[0]  # cycle
    node = loop_delete(ll[0], m)
    print node.data

if __name__ == '__main__':
    main(5, 3)
    calculate(5, 3)
