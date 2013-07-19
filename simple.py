#!/usr/bin/python

# Python notes based on Writing Idiomatic Python by Jeff Knupp
# Use Python Package Index (PyPI)
# Use pip install <name-of-package>
# Use itertools module
# Use os.path module

# global variables should be in CAPS (3.1.1)
SECONDS_IN_A_DAY = 60 * 60 * 24


def myfunc(var):
	""" prints value stored in variable (3.2.1.2) """
	print var



# Use the if __name__ == '__main__' pattern to allow a file to be both
# imported and run directly (3.5.1)

# Will only run if script is executed directly,
# not when the file is imported as a module
if __name__ == '__main__':
	str = 'Hello World'
	myfunc(str)

	print SECONDS_IN_A_DAY
	
