#!/usr/bin/python

from __future__ import print_function
import sys

def main():

	

	# open the file
	file = open('syslog')

	#reads only one line
	log_data = file.readline()

	# reads entire file
	log_data = file.readlines()


	print(log_data)

	# close the file
	file.close

if __name__ == '__main__':
	sys.exit(main())

