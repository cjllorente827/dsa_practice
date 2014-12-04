
''' 
Space complexity: O(n) 
Search: O(log n) - O(n)
Insert: O(log n) - O(n)
Delete: O(log n) - O(n)
'''

from queue import Queue

class BinaryTree:

	def __init__(self):
		self.root = None

	def insert(self, value):
		if self.root is None:
			self.root = Node(value)
			return
		if value == self.root.value:
			return

		node = self.root 
		while True:
			if value == node.value: #because the value exists in the BST already and we have found it here
				return

			if value < node.value:
				if node.lt is None:
					node.lt = Node(value)
					return
				node = node.lt
			else:
				if node.gt is None:
					node.gt = Node(value)
					return
				node = node.gt

	def contains(self, value):
		node = self.root
		while node is not None:
			if value == node.value:
				return True
			elif value < node.value:
				node = node.lt
			else:
				node = node.gt
		return False

	def __str__(self):
		return ' '.join([str(x) for x in self.traverse_breadth()])

	#traverses the tree breadth-first and returns an array of arrays
	#each index marks the depth at which the value was found
	#each sub-array contains all values found at that depth
	def traverse_breadth(self):
		if self.root is None:
			return []

		q = Queue()
		q.push(self.root)		
		values = []
		while not q.is_empty:
			node = q.pop()
			values.append(node.value)
			if node.lt is not None:
				q.push(node.lt)
			if node.gt is not None:
				q.push(node.gt)
		return values

class Node:
	def __init__(self, init_val):
		self.value = init_val
		self.gt = None 
		self.lt = None

	def __gt__(self, other):
		return self.value > other.value

	def __lt__(self, other):
		return self.value < other.value

	def __eq__(self, other):
		return self.value == other.value

	def __ne__(self, other):
		return self.value != other.value

	def __str__(self):
		return str(self.value)

