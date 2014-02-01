#coding=utf-8
"""
remove duplicates from an unsorted linked list
with or without tmporary buffer
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs import linkedlist 

def remove1(node):
	"""with buffer"""
	b = []
	last = None
	while node:
		if node.data not in b:
			b.append(node.data)
		else:
			if last:
				last.next = node.next
		last = node
		node = node.next

def remove2(node):
	"""without buffer"""
	while node:
		node2 = node.next
		last = node
		while node2:
			if node2.data == node.data:
				last.next = node2.next
			last = node2
			node2 = node2.next
		node = node.next
	pass

if __name__ == '__main__':
	node = linkedlist.array2linkedlist([1,1,2,3,4,5,6,6,7,8,8,9,9])
	remove1(node)
	for i in node:
		print i.data, 
	print ""
	node = linkedlist.array2linkedlist([1,2,3,4,5,6,6,7,8,8,9,9])
	remove2(node)
	for i in node:
		print i.data, 
	print ""
