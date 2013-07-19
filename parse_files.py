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


	# 'r' stands for raw and is simply an indicator to Python that no string
	# interpolation should be performed on the string

	# another way to read file line-by-line
	pattern = 'Jul 16' # use re.match for beginning of line only
	#pattern = 'CRON' # use re.search to match anywhere
	with open('syslog', 'r') as f:
		for line in f:
			match = re.match(pattern, line)
			if match:
				print (line)

	pattern = re.compile("d")
	pattern.search("dog")
	if pattern.search:
		print ('Match found')

	

if __name__ == '__main__':
	sys.exit(main())

