"""
convert a binary tree to double linked list
"""
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs import binary_tree

def convert(root):
	a, b, c, d = root, root, root, root
	if root.left:
		a, b = convert(root.left)
		root.left = b
		b.right = root
	if root.right:
		c, d = convert(root.right)
		root.right = c
		c.left = root
	return a, d


def main():
	n = binary_tree.array2tree([10,6,14,4,8,12,16])
	a,d = convert(n)
	tmp = a
	while tmp:
		print tmp.data
		tmp = tmp.right

if __name__ == '__main__':
	main()

