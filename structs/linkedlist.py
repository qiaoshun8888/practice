#coding=utf-8

def array2linkedlist(array, need_array=False):
	for k, v in enumerate(array):
		array[k] = Node(v)
		if k > 0:
			array[k-1].next = array[k]
	if need_array:
		return array
	return array[0]

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
	n = array2linkedlist([1,2,3,4,5,6,7,8,9])
	for i in n:
		print i.data
