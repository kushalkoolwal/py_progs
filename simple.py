#!/usr/bin/env python

# Python notes based on Writing Idiomatic Python by Jeff Knupp
# Use Python Package Index (PyPI)
# Use pip install <name-of-package>
# Use itertools module
# Use os.path module

# use function-based version of print (1.3.3)
from __future__ import print_function
import sys


# global variables should be in CAPS (3.1.1, 3.1.2/PEP8)
SECONDS_IN_A_DAY = 60 * 60 * 24


# variables and functions should be joined with underscore (3.1.2/PEP8)
def print_func(var):
	""" prints value stored in variable (3.2.1.2) """
	print (var)


def calculate_mean (num_list):

	return sum(num_list) / len(num_list)


def swap (a, b):
	# no need to use extra variable (2.1.1)
	(a, b) = (b, a)
	print (a, b)
	# python returns multiple values as tuples
	return a, b

# always create main function for your program (3.5.2)
def main():
	""" main function of the program """
	num1 = 5
	num2 = 6

	str = 'Hello World'
	print_func(str)

	print (SECONDS_IN_A_DAY)

	# Lists are like arrays
	# use 'in' keyword for iterables (1.2.2)
	num_list = [10, 20]
	for num in num_list:
		print (num)

	# interate by index in for loop
	for index in range(len(num_list)):
		print ('Num:', num_list[index])

	print (calculate_mean(num_list))

	# Tuples are read-only lists	
	name_tuple = ('Kushal', 'Koolwal', 'KK')
	# use enumerate (1.2.1)
	for index, name in enumerate(name_tuple):
		print ('{} {}'.format(index, name))
	# 'for' and 'while' loops have else statement (1.2.3)
	else:
		print ("All names are were printed")

	swap(num1, num2)
	print (num1, num2)

	# Success = 0; Error = Other
	sys.exit(0)

	# return below is optional if you have sys.ext(0), as default return value
	# in python is 'None' which sys.exit treats as 'exit with 0'.
	return 0
	
# Use the if __name__ == '__main__' pattern to allow a file to be both
# imported and run directly (3.5.1)

# Will only run if script is executed directly,
# not when the file is imported as a module
if __name__ == '__main__':
# call sys.exit with return value of main function as the parameter (3.5.2).
	sys.exit(main())
