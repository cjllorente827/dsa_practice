#!/usr/bin/env python
class Queue:

	def __init__(self):
		self.q = []
		self.is_empty = True

	def push(self, x):
		self.q.append(x)
		self.is_empty = False

	def pop(self):
		r = self.q[0]
		self.q = self.q[1:]
		self.is_empty = True if len(self.q) == 0 else False
		return r

	def __str__(self):
		return ' '.join([str(x) for x in self.q])

def run_tests():
	q = Queue()
	q.push(10)
	q.push(5)
	q.push(15)
	q.push(2)
	q.push(7)
	q.push(12)
	q.push(20)
	print(q)

	print(q.pop())
	print(q.pop())
	print(q.pop())
	print(q.pop())

	print(q)

if __name__ == '__main__':
	run_tests()