""" This is the python script that is
	used to display basic string 
	manipulation operations."""

def cat_string(str1, str2):
	return str1+str2

def repeat_string(str1, num_repeat):
# The specified string will be repeated num_repeat times
	return str1*num_repeat

def find_presence(str1, str2):
#Check whether a character is present in the string or not
	return str2 in str1

def get_middle_char(str1):
#Retuns the middle character of the string
	str_len = len(str1)
	mid_idx = str_len / 2
	return str1[mid_idx]

def get_specified_char(str1, idx):
#Returns whether the specified character is present in the given string
	return str1[idx]

def get_sub_str(str1, start_idx, end_idx):
# Returns he substring between start and end index
	if start_idx < 0:
		start_idx = 0
	if end_idx > len(str1):
		end_idx = len(str1) - 1
	return str1[start_idx : end_idx]

# These are the test stream. We can very easily replace these streams with any user given strings
string_sq = 'This is an awesomely single quoted string'
string_non_space = 'ThisIsAStringWithoutSpace'
string_dq = "This is a double quoted string"
string_tq = """ This is a triple quoted string"""

print "Adding single quoted and double quoted string : \"%s\""%cat_string(string_sq, string_dq)

num_str_repeat = int(raw_input("Enter the numbmer of times you want the strin to be repeated : "))
print "Now we will repeat triple quoted string : \"%s\""%repeat_string(string_tq, num_str_repeat)

check_char = raw_input("Enter the char you want to check : ")
if find_presence(string_sq, check_char):
	print "The string contains the character sought for"
else:
	print "The string does not contain the character sought for"

print "Middle character of \"%s\" is \'%s\'"%(string_sq, get_middle_char(string_non_space))

index = int(raw_input("Enter the index of character you want : "))
print "%d th character of \"%s\" is \'%s\'"%(index, string_dq, get_specified_char(string_dq, index))

start_index = int(raw_input("Enter starting index of substring : "))
end_index = int(raw_input("Enter the ending index of substring : "))
print "substring of \"%s\" from %d to %d is \"%s\""%(string_tq, start_index, end_index, get_sub_str(string_tq, start_index, end_index))

# End of Script