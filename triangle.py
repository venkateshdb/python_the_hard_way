#program to summrise what i have learned so far.
print "use to display output in the screen"
print "sting is simle set of letters \n comes between quotes,\n they can be single or double,but should start and end with same."
print "strings can be formatted by using string formatters"
print "variables are just like storage box\n that stores the given data into a specific box or block"
print "for defining variables in python we use assignment (=) symbol into it.\nsome rules for defining a variable\1)shoukd start with a letter,no number,special character to be used for staring tvariable\n use of undeescore(_) for giving space inbetween."
#using variables
x = 'python\t'
y = 'is\t'
z = 'awesome\t'
print  x + y +z # thsi is known as sting contennation
#use of string formmatters
print "there is large amount of string formatters in python\nbut i will discuss the one i have learned nicely.\n"
print """
1) %s , %d , %r %s is use for strings, %d is used for number , %r is providers raw data form the program ,and for using we put %(and assing value.)
2){} work similar as above but for using them we use .format(value to be assigned.)
3)use of backslash \" to for quotes
"""
print "this is double quote inside 5\"36\" and finished "
print """
use of argv
arguments1,arguments2,.... = argv # unpacking the arguments.
now using it it any where
"""
def get_input1(a,b):
    print "printing the sum of %d , %d"  %(a,b)
    return get_input1
get_input1(43,434)
c = get_input1(43,434   )
print c
