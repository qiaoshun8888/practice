#coding=utf-8
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs import binary_tree

def find(node, with_sum, realsum, path=[]):
	# print node.data, with_sum, realsum, path
	path.append(node.data)
	if node.data == with_sum:
		yield path

	if node.left:
		for i in find(node.left, with_sum-node.data, realsum, path):
			yield i
		for i in find(node.left, realsum, realsum, []):
			yield i
	if node.right:
		for i in find(node.right, with_sum-node.data,realsum, path):
			yield i
		for i in find(node.right, realsum, realsum, []):
			yield i
	path.pop()



def main():
	node = binary_tree.array2tree([10, 5, 12, 4, 7, 10])
	for i in find(node, 22, 22):
		print i

if __name__ == '__main__':
	main()

