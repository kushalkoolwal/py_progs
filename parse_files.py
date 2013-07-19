#!/usr/bin/python

from __future__ import print_function
import sys

def main():

	

	# open the file
	file = open('syslog')

	# reads entire file into memory
	# not good for large files
	log_data = file.readlines()

	#log_data = file..readlines()[4:] # skips first 4 lines

	# close the file
	file.close

	print(log_data)

	# read file line-by-line
	for line in open('syslog', 'r'):
		print (line)
	


if __name__ == '__main__':
	sys.exit(main())

