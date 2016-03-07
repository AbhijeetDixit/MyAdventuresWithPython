""" This file will simply create a class
	and instantiate it in main function to
	demonstrate the use of classes """

class Employee:
	'This is a base class for an employee of an educational institution'
	empCount = 0
	def __init__(self, name, age, desig):
		self.name = name
		self.age = age
		self.designation = desig
		Employee.empCount += 1
		pass

	def displayCount(self):
		print "Total employees : %d"%Employee.empCount
		pass

	def displayemployee(self):
		print "name : %s\nage : %d\ndesignation:%s\n"%(self.name, self.age, self.designation)
		pass

if __name__ == "__main__":
	emp1 = Employee('Employee1', 21, 'Engineer')
	print 'Employee 1 is as follows:'
	emp1.displayemployee()
	emp1.displayCount()

	emp2 = Employee('Employee2', 44, 'Manager')
	print '\n\nEmployee 2 is as follows:'
	emp2.displayemployee()
	emp2.displayCount()
	pass