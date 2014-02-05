"""
implement next (in-order)
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs import binary_tree

if __name__ == '__main__':
	l = binary_tree.array2tree([1,2,3,4,5,6,7,8,9], True)
	node = l[-2]
	while node:
		print node.data,
		node  = node.in_order_next()
	print ""
	for i in l[0].in_order():
		print i,
