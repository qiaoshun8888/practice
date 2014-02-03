"""
a function to check if a btree is balanced
"""


import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs.btree import Node


def is_balance(node):
	ed = []
	def dfs(node, deep):
		if node not in ed:	
			ed.append(node)
			if not node.left and not node.right:
				yield deep
			else:
				if node.left:
					for i in dfs(node.left, deep+1):
						yield i
				if node.right:
					for i in dfs(node.right, deep+1):
						yield i
	m = float('-inf')
	n = float('inf')
	for i in dfs(node, 0):
		if i > m:
			m = i	
		if i < n :
			n = i
		if m - n >= 2:
			return False

	return True


def main():
	n1 = Node(1)
	n2 = Node(2)
	n3 = Node(3)
	n4 = Node(4)
	n5 = Node(5)
	n1.left = n2
	n1.right = n3
	n2.left = n4 
	n4.left = n5
	print is_balance(n1)

if __name__ == '__main__':
	main()
