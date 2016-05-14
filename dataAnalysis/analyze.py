import csv
import sys

def read_csv(filepath):
	print "Filepath is %s"%filepath
	try:
		f_ob = open(filepath,'rb')
		new_data_list = []
		try:
			csv_ob = csv.reader(f_ob)
			for row in csv_ob:
				new_data_list.append(row)
				pass
		except Exception, e:
			raise e
		pass
		f_ob.close()
		pass
	except Exception, e:
		raise e
	return new_data_list

def process_data(filepath):
	data_list = read_csv(filepath)
	print data_list
	print "\nSorting the List\n"
	sorted(data_list,key=itemgetter(0))		#Sorting on the first coloumn
	pass

if __name__ == "__main__":
	process_data(sys.argv[1])