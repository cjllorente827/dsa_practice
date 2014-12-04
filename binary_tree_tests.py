#!/usr/bin/env python
from binary_tree import BinaryTree
import timeit

def run_tests():
	print("Running tests for Binary Search Tree")
	bst = BinaryTree()
	bst.insert(10)
	bst.insert(5)
	bst.insert(15)
	bst.insert(2)
	bst.insert(20)
	bst.insert(12)
	bst.insert(7)
	print(bst)

	assert(bst.contains(10))
	assert(bst.contains(20))
	assert(not bst.contains(50))
	assert(not bst.contains(3))
	assert(bst.contains(2))
	assert(not bst.contains(1))

	print("All tests passed!")

if __name__ == '__main__':
	run_tests()