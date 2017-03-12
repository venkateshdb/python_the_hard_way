#code for copying files.
from sys import argv
print "-------------------------------------------"
print "now lets copy content from file"
print "-------------------------------------------"
script , copy_from , copy_to = argv
print "we are going to copy this file %s" % copy_from
print "To this file %s" % copy_to
x = open(copy_from , "a+") # file from where we are steling things
y = open(copy_to , "a+") # file where we are going to hide things
data =  x.read() #stelling data and loading it in data named car.
y.write(data) #now hiding this data.
x.close()
y.close()
print "copying to file completed!!!!"
