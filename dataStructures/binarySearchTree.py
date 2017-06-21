__author__ = 'Abhijeet'

class Node(object):
	"""docstring for Node"""
	def __init__(self, val):
		self.left = None
		self.right = None
		self.value = val


class BinarySearchTree(object):
	"""docstring for BinarySearchTree"""
	def __init__(self):
		self.root = None

	def _add(self, node, val):
		if node == None:
			node = Node(val)
		else:
			if node.value < val:
				if self.root.left == None:
					self.root.left = Node(val)
				else:
					_add(node.left, val)
			else:
				if self.root.right == None:
					self.root.right = Node(val)
				else:
					_add(node.right, val)
				pass
		pass

	def add(self, val):
		if self.root == None:
			self.root = Node(val)
		else:
			#Add it to proper place.
			if val < self.root.value:
				if self.root.left == None:
					self.root.left = Node(val)
				else:
					self._add(self.root.left, val)
				pass
			else:
				if self.root.right == None:
					self.root.right = Node(val)
				else:
					self._add(self.root.right, val)
			pass
		pass

	def search(self, val):
		node = self.root
		while node != None:
			if val == node.value:
				print "Element found in tree"
				break
			elif val < node.value:
				node = node.left
			else:
				node = node.right
				pass
			pass
		pass
		if node == None:
			print "Element not found"

	def delete(self, val):
		pass

	def _inTraversal(self, node):
		if node == None:
			return
		self._inTraversal(node.left)
		print node.value
		self._inTraversal(node.right)
		pass

	def inOrderTraversal(self):
		self._inTraversal(self.root.left)
		print self.root.value
		self._inTraversal(self.root.right)
		pass

	def _preOrderTraversal(self, node):
		if node == None:
			return
		self._preOrderTraversal(node.left)
		self._preOrderTraversal(node.right)
		print node.value
		pass

	def preOrderTraversal(self):
		self._preOrderTraversal(self.root.left)
		self._preOrderTraversal(self.root.right)
		print self.root.value
		pass

	def _postOrderTraversal(self, node):
		if node == None:
			return
		print node.value
		self._postOrderTraversal(node.left)
		self._postOrderTraversal(node.right)
		pass

	def postOrderTraversal(self):
		print self.root.value
		self._postOrderTraversal(self.root.left)
		self._postOrderTraversal(self.root.right)
		pass

def printMenu():
	print "********** Binary Search Tree **********"
	print "1. Add a node"
	print "2. Search a value"
	print "3. Delete a value"
	print "4. In Order Traversal"
	print "5. Pre Order Traversal"
	print "6. Post Order Traversal"
	print "0. Exit"
	return int(input("Enter your choice : "))

if __name__ == '__main__':
	tree1 = BinarySearchTree()
	ch = printMenu()
	while ch != 0:
		if ch == 1:
			tree1.add(int(input("Enter the value to be added : ")))
			print "Added to the tree"
			pass
		elif ch == 2:
			tree1.search(int(input("Enter the value to be searched : ")))
		elif ch == 4:
			tree1.inOrderTraversal()
		elif ch == 5:
			tree1.preOrderTraversal()
		elif ch == 6:
			tree1.postOrderTraversal()
		else:
			print "Not implemented"
		pass
		ch = printMenu()