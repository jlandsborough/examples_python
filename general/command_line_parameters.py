#! /usr/bin/python

## Jason Landsborough
## Last updated: 7/4/2013
##
## Example of how to use command line parameters
##
## Usage: python command_line_paramters.py p1 p2 p3
##
## Example usage: python command_line_parameters hi test


import sys #needed for sys.argv

#Print the first element of the sys.argv list
print "sys.argv[0]:", sys.argv[0]	#index 0 is the file name

#check length of sys.argv to find if any paramters were given
if(len(sys.argv) == 1):
	print "No paramters given, quitting"
	exit()

#If a parameter was given, display what the first parameter was
if(len(sys.argv) > 1):
	print "The first parameter at sys.argv[1] is:",  sys.argv[1] 



#Look for a given parameter test in the list of parameters
if("test" in sys.argv):
	test_index = sys.argv.index("test")	#get the index
	print "The parameter 'test' found at index", test_index #display result


