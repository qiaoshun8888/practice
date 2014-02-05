"""
common ancestor
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs import binary_tree


def common_ancestor(node1, node2):
	deep1 = 0
	deep2 = 0
	tmp1 = node1
	tmp2 = node2
	while tmp1.parent:
		deep1 += 1
		tmp1 = tmp1.parent

	while tmp2.parent:
		deep2 += 1
		tmp2 = tmp2.parent

	if deep1 > deep2:
		for i in range(deep1 - deep2):
			node1 = node1.parent
	elif deep1 < deep2:
		for i in range(deep2 - deep1):
			node2 = node2.parent

	while not node1 == node2:
		if not node1.parent or not node2.parent:
			return -1
		node1 = node1.parent
		node2 = node2.parent
	return node1.data

def main():
	l = binary_tree.array2tree([1,2,3,4,5,6,7,8,9], True)
	print l[7].data
	print l[4].data
	print common_ancestor(l[7], l[4])



if __name__ == '__main__':
	main()
