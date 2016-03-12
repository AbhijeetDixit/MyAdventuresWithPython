''' This example shows the use of multiple classes in a single program'''

class City:

	def __init__(self, name):
		self.name = name
		self.instituteCount = 0
		self.instituteList = []
		pass

	def addInstitute(self, instObj):
		self.instituteList.append(instObj)
		self.instituteCount += 1

	def displayInstitute(self):
		print 'instituteCount %d'%self.instituteCount
		for inst in self.instituteList:
			inst.displayInfo()
			pass

	def displayCity(self):
		print '________________ City ________________'
		print 'CityName : %s'%self.name
		print 'City Institutes'
		self.displayInstitute()


class institute:

	def __init__(self, name):
		self.name = name
		self.numDepts = 0
		self.depts = []

	def addDepts(self, deptname):
		self.depts.append(deptname)
		self.numDepts += 1

	def displayInfo(self):
		print 'name : %s'%self.name
		print 'dept Count : %d'%self.numDepts
		i = 0
		for dept in self.depts:
			print '%d. %s'%(i+1, dept)

if __name__ == '__main__':
	city1 = City('Bangalore')
	institute1 = institute('IISc')
	city1.displayCity()
	institute1.displayInfo()

	print '\nAdding depts\n'

	institute1.addDepts('CSE')
	institute1.addDepts('Chemical')

	institute1.displayInfo()

	print '\nAdding institute\n'

	city1.addInstitute(institute1)

	city1.displayCity()