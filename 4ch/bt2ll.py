
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from structs.btree import array2tree
from structs.btree import Node as TNode
from structs.linkedlist import Node as LNode



def bfs(root):
	res = {}
	queue = []
	queue.append((root, 0))
	while queue:
		node, deep = queue.pop(0)
		if deep not in res:
			res[deep] = LNode(node.data)
		else:
			lnode = res[deep]
			while lnode.next:
				lnode = lnode.next
			lnode.next = LNode(node.data)

		if node.left:
			queue.append((node.left, deep+1))
		if node.right:
			queue.append((node.right, deep+1))
	return res

def main():
	root = array2tree([1,2,3,4,5,6,7,8,9,0])
	res = bfs(root)

	keys = res.keys()
	keys.sort()
	for k in keys:
		print k, 
		for i in res[k]:
			print i.data, 
		print ""


if __name__ =='__main__':
	main()

