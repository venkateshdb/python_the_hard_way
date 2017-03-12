#more ways to use function
def part_time(food,place):
    print 'what amount of %s food we have \n and and the palace we are going for partying is %s ' % (food,place)
stomach = 'soft-drinks,snacks,cakes,wafers,biscuits,cookies and much more'
roaming = 'leh,rajasthan,delhi,lonavala and sahydri mountains,south side and east part of india'
part_time(stomach,roaming)
def maths(add,sub):
    print 'add %d , sub %d' %(add,sub)
jun = 6
may = 5
maths(jun+3, may+30)
################################################################################
def frameworks(a,b,c,d,e,f,g,h,i,j,k): #making a simple function.
    print "list of web frameworks to make your work easy   \n%s\n %s\n %s\n %s\n %s\n %s\n %s\n %s\n %s\n %s\n %s\n" % (a,b,c,d,e,f,g,h,i,j,k) #simple sting.
#calling this function in different ways.
l1 = "django"
l2 = "flask"
l3 = "backbone.js"
frameworks("node.js", "angularjs", "d3.js", "two.js" , "bootstrap" , "mdl by google","angularjs","jquery",l1,l2,l3)
#when you get this error Traceback (most recent call last):
  #File "C:\Users\admin\Documents\learn\ex19.py", line 16, in <module>
    #frameworks("node.js", "angularjs", "d3.js", "two.js" , "bootstrap" )
  #File "C:\Users\admin\Documents\learn\ex19.py", line 14, in frameworks
    #print "list of web frameworks to make your work easy %s , %s" % (a,b,c,d) #simple sting.
#TypeError: not all arguments converted during string formatting
###$%@@@@ in my case it was because of less no of string formates used.
def get(w,e):
    print "can we use now in palce of var for func %r ,%r" % (w ,e)
o = int(raw_input('one no.>>'))
p = int(raw_input("second no.>>"))
res = ag =  o+p
get(res ,ag)
