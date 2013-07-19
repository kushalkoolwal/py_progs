#!/usr/bin/env python

from __future__ import print_function
import sys
import re

def main():

	

	# open the file
	file = open('syslog')

	# reads entire file into memory
	# not good for large files
	log_data = file.readlines()
	#log_data = file..readlines()[4:] # skips first 4 lines

	# close the file
	file.close

	#print(log_data)

	# read file line-by-line
	#for line in open('syslog', 'r'):
	#	print (line)

	# another way to read file line-by-line
	pattern = '^Jul 16'
	with open('syslog', 'r') as f:
		for line in f:
			if re.match(pattern, line):
				print (line)

if __name__ == '__main__':
	sys.exit(main())

