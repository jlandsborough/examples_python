#! /usr/bin/python

## Jason Landsborough
## Last updated: 8/5/2013
##
## Example of how to traverse directories and files recursively
##
## Usage: python recursive_traversal.py
##
## 


import os #needed for os.walk()

target_dir = os.getcwd()  #set to some other directory that has subfolders and files

#go through directory and subdirectories, variables dirs and files are lists
for curdir, dirs, files in os.walk(target_dir):
		print "current directory: " + str(curdir)
		print "subdirectories: " + str(dirs)
		print "files: " + str(files)  
		print


