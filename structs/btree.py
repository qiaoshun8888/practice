#coding=utf-8

def array2tree(l):
	for k, v in enumerate(l):
		l[k] = Node(v)
	for i in range(len(l)/2):
		if 2*i + 1 < len(l):
			l[i].left = l[i *2+1]
		if 2*i + 2 < len(l):
			l[i].right = l[i*2+2]
	return l[0]


class Node(object):
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


	def pre_order(self):
		yield self.data
		if self.left:
			for i in self.left.pre_order():
				yield i
		if self.right:
			for i in self.right.pre_order():
				yield i

	def in_order(self):
		if self.left:
			for i in self.left.in_order():
				yield i
		yield self.data
		if self.right:
			for i in self.right.in_order():
				yield i

	def post_order(self):
		if self.left:
			for i in self.left.post_order():
				yield i
		if self.right:
			for i in self.right.post_order():
				yield i
		yield self.data

if __name__ == '__main__':
	n1 = Node(1)
	n2 = Node(2)
	n3 = Node(3)
	n4 = Node(4)
	n5 = Node(5)
	n6 = Node(6)
	n7 = Node(7)
	n1.left = n2
	n1.right = n3
	n2.left = n4
	n2.right = n5
	n3.left = n6
	n3.right = n7

	for i in n1.pre_order():
		print i,
	print ""

	for i in n1.in_order():
		print i,
	print ""

	for i in n1.post_order():
		print i,
	print ""

	print array2tree([10,6,14,4,8,12,6]).data


