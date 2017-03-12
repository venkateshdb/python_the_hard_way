#using readline
from sys import argv
script , file_name = argv
current_file = open(file_name)
def all(p):
    print p.read()

def line_wise(p):
    print p.readline()
print "whole file\n"
all(current_file)
def rewind(p):
     p.seek(0)
rewind(current_file)
print "line_wise\n"
line_wise(current_file)
line_wise(current_file)
line_wise(current_file)
