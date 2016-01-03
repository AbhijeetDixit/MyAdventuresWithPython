""" This script is just for playing
	with the verious control statements
	in python"""

def print_nonspace_chars_with_newline(str1):
# This function prints all the non space characters
# in the given string in a newline. It skips spaces
	for ch in str1:
		if ch == ' ' or ch == '\n' or ch == '\t':
			continue
		else:
			print ch

def repeat_nth_character_nplus1_times(str1):
# This function prints all the characters in the 
# string pos number of times, where pos is the 
# position of next character in the string
	pos = 0
	length = len(str1)
	while pos < length:
		print str1[pos]*(pos+1)
		pos += 1

def repeat_strings_from_string_array(arr1):
# This function takes in a string array as an input
# and prints each of the string multiplied by next pos
	counter = 1
	for string in arr1:
		print string*counter
		counter += 1
	else:
		print "Done with all the printing stuff"	# Else when used with for loop, is executed when for loop is completed


print "This script does the following things:"
print "\t1. Print every non space characters in the string in a new line"
print "\t2. repeat every character in string n+1 times where n is its position in string"
print "\t3. Repeat strings from string array n+1 times where n is its position in array"
user_choice = int(raw_input("Enter what you wanna do : "))

if user_choice != 1 and user_choice != 2 and user_choice != 3:
	print "Duh!! You failed to enter a correct choice. good bye!"
else:
	if user_choice != 1 and user_choice !=2:
		arr1 = []
		num_elements = (int(raw_input("Enter the number of elements you want in array : ")))
		for i in range(0,num_elements):
			string = raw_input("Enter the element : ")
			arr1.append(string)
		repeat_strings_from_string_array(arr1)
	else:
		string = raw_input("Enter your string : ")
		if user_choice == 1:
			print_nonspace_chars_with_newline(string)
		else:
			repeat_nth_character_nplus1_times(string)