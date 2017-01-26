__author__ = 'Abhijeet'

class Stack(object):
	maxSize = 0
	data = []

	def __init__(self, maxSize):
		self.maxSize = maxSize
		self.data = []
		print "Stack created"

	def top(self):
		return data[0]

	def push(self, value):
		if len(self.data) == self.maxSize:
			print "Stack overflow"
		else:
			self.data.append(value)
			print "Element pushed"

	def pop(self):
		if len(self.data) == 0:
			print "Stack Underflow"
		else:
			value = self.data.pop()
			return value

	def displayStack(self):
		print self.data

def printMenu():
	print "\n**********This is stack menu************"
	print "1. Initialize a stack."
	print "2. Push an element to stack"
	print "3. Pop an element from stack"
	print "4. Print topmost element"
	print "0. Exit"
	ch = int(input("Enter your choice : "))
	return ch

if __name__ == '__main__':
	initialized = False
	while True:
		ch = printMenu()
		if ch == 0:
			break
		elif ch == 1:
			if initialized:
				print "Already initialized"
			else:
				stack1 = Stack(int(input("Enter the max size of stack : ")))
				initialized = True
		elif ch == 2:
			if not initialized:
				print "Stack not created"
			else:
				stack1.push(int(input("Enter the element to be entered : ")))
				stack1.displayStack()
		elif ch == 3:
			if not initialized:
				print "Stack not created"
			else:
				print stack1.pop()
			#stack1.displayStack()
		elif ch == 4:
			if not initialized:
				print "Stack not created"
			else:
				print stack1.top()
	pass