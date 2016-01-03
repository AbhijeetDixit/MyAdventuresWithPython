""" This script will depict some beginner
	level file operations in pyhton"""

def read_file_to_console(file_name):
# Prints the contents of file to console
	file_handle = open(file_name, "r")
	print file_handle.read()
	file_handle.close()

def write_string_to_file(file_name, str1):
# writes contents to a file.
	file_handle = open(file_name, "w")
	file_handle.write(str1)
	file_handle.close()
	
def copy_file(file_from, file_to):
# copy contents from one file to another
	file_handle_from = open(file_from, "r")
	file_handle_to = open(file_to, "w")
	file_handle_to.write(file_handle_from.read())
	file_handle_from.close()
	file_handle_to.close()

file_name_to_read = raw_input("Enter the filename to read : ")
read_file_to_console(file_name_to_read)

file_name_to_write = raw_input("Enter the filename to write : ")
string_to_write = raw_input("Enter the string to write to file : ")
write_string_to_file(file_name_to_write, string_to_write)

source_file = raw_input("Enter the file from which to copy : ")
dest_file = raw_input("Enter the file to which copy is to be done : ")
copy_file(source_file, dest_file)