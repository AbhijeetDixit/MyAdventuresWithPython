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

def main():
	print 'Creating a new City'
	cName = raw_input('Enter City Name : ')
	city1 = City(cName)
	print 'Displaying new City Information'
	city1.displayCity()

	print 'Creating a new institute'
	iName = raw_input('Enter the name of institute : ')
	institute1 = institute(iName)
	print 'Displaying newly created institute'
	institute1.displayInfo()
	response = raw_input('Should we add institute to the created city? (y/n) : ')
	if response == "y" or response == "Y":
		city1.addInstitute(institute1)
		print 'The created city now becomes'
		city1.displayCity()
		pass

	print 'We need to add atleast 2 depts in the institute'
	dept1 = raw_input('Add first dept name : ')
	institute1.addDepts(dept1)
	dept2 = raw_input('Add second dept name : ')
	institute1.addDepts(dept2)

	if response == "y" or response == "Y":
		print 'The city now becomes : '
		city1.displayCity()
	else:
		print 'The new department becomes : '
		institute1.displayInfo()


if __name__ == '__main__':
	main()