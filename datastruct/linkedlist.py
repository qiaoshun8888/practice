#coding=utf-8

class Node(object):
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next
	
	def append(self, node):
		n = self
		while n.next:
			n = n.next
		n.next = node
	
	def insert(self, node):
		n = self
		tmp = n.next
		n.next = node 
		n.next.next = tmp

	def __iter__(self):
		n = self
		while n:
			yield n
			n = n.next

if __name__ == '__main__':
	n1 = Node(1)
	n2 = Node(2)
	n3 = Node(3)
	n4 = Node(4)

	n1.append(n2)
	n1.insert(n3)
	n1.append(n4)
	for n in n1:
		print n.data
