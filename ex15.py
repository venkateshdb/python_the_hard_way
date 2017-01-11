print "####################################"
# including write,read utility to file
print "# v.3 file_system utility          # "
print "####################################"
print "read  my source code using it easily"
#from sys import argv
#script , filename = argv
print """
-----------------------------------------
\tList of pyhton scripts to read!!
-----------------------------------------
1)ex1.py\n
2)ex2.py\n
3)ex3.py\n
4)ex4.py\n
5)ex5.py\n
6)ex6.py\n
7)ex7.py\n
8)ex8.py\n
9)ex9.py\n
10)ex10.py\n
11)ex11.py\n
12)ex12.py\n
13)ex13.py\n
14)ex14.py\n
15)ex15.py\n
15)ex15.txt\n
16)ex16.py\n
16)ex16.txt\n
17)zork.py\n
"""
filename = raw_input(
    "type filename you want to read,use ex15.txt for now>>")  # getting filename for reading
# opening the file,assigning the variable a function
todo = open(filename, 'a+')
print "we are going to read this file %s" % filename  # simple sting in pyhton
do = raw_input("write here to write in the file>>")  # v1.2
todo.write(do)
raw_input("want to read that file,if yes press enter dont want to read ctrl+c")
todo.close()
# reopening file for reading
todo = open(filename)
print todo.read()
