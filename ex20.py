#using file with function
#from sys import argv
#script , file_to = argv
#    print "using this script %s and file %s" %(script,file_to)
#tip = open(file_to , "a+")
#def read_loud(reading):
#    print tip.read()
#read_loud('call')
from sys import argv
script , input_file = argv
current_file = open(input_file , "a+")
def printing(f):
     print f.read()
def rewind(f):
     f.seek(0)
def print_a_line(line_count , f):
    print line_count , f.readline()

print 'now lets print whole file.\n:'
printing(current_file)
print "now lets rewind like a tape"
rewind(current_file)
print "lets print these again.\n"
current_line  = 1
print_a_line(current_line , current_file)
current_line += 1
print_a_line(current_line,current_file)
current_line += 1
print_a_line(current_line , current_file)
current_file.close()
