#coding=utf-8

class Node(object):
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


	def in_order(self):
		if self.left:
			for i in self.left.in_order():
				yield i
		yield self.data
		if self.right:
			for i in self.right.in_order():
				yield i


if __name__ == '__main__':
	n1 = Node(1)
	n2 = Node(2)
	n3 = Node(3)
	n1.left = n2
	n1.right = n3

	for i in n1.in_order():
		print i
