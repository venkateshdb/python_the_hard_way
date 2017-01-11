# using truncate for cleaning the file
# using argumnet for getting file .
# aading a new feature to tell file size
# v1.2
from sys import argv
script = argv  # takes argument from command line
print('----------------------------------------------')
print 'This utility helps you to clean files easily'
print('-----------------------------------------------')
print 'Are you sure you want to procced\nYES:press enter\nNO:use ctrl+c'
raw_input()
# read = open(filename , 'w+') # assigning variab;e a simple function.
clean = raw_input('Type the filename to clean>>')
file_clean = open(clean, 'w+')
print 'your file %s %d bytes long' % (clean, len(clean))
file_clean.truncate()
print 'your file {} is cleaned' .format(clean)
file_clean.close()
# mistakes i have done
# at 11 line called a function on calling method
# at line 8 didn't opend file for in writing mode
