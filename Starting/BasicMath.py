""" This is a simple beginner level python script
	that displays basic mathematical operations in
	python2.x. Appropriate comments are placed."""

def add(var1, var2):
	return (var1 + var2)

def subtract(var1, var2):
	return (var1 - var2)

def multiply(var1, var2):
	return (var1 * var2)

def divide(var1, var2):
	if var2 == 0:
		return "Division by 0 not allowed"
	else:
		return (var1 / var2)

def absolute_diff(var1, var2):
	if var1 > var2:
		return (var1 - var2)
	else:
		return (var2 - var1)

def reorder(var1, var2):
	""" This function returns the 
	operands in decreasing order"""
	if var1 > var2:
		return var1, var2
	else:
		return var2, var1

print "This is a simple mathematical menu"
print "You have following options:"
# Following is the example of multiline printing in python without use of \n
print """ 1. Add
2. Subtract
3. multiply
4. divide
5. absolute_diff
6. reorder"""

int1 = int(raw_input("Enter first operand:\t"))		# typecasting input to integer
int2 = int(raw_input("Enter second operand:\t"))
operator = int(raw_input("Enter operation you want to perform:\t"))

if operator == 1:
	print add(int1, int2)
elif operator == 2:
	print subtract(int1, int2)
elif operator == 3:
	print multiply(int1, int2)
elif operator == 4:
	print divide(int1, int2)
elif operator == 5:
	print absolute_diff(int1, int2)
elif operator == 6:
	val1, val2 = reorder(int1, int2)
	print "Bigger number is = %d\n Smaller number is = %d\n"%(val1, val2)
else:
	print "Invalid choice"