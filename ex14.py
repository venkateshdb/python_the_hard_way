from sys import argv
script , user = argv
print "hello %s" % user
prompt = '>'
print 'we are trying to combine what we have learned using this file' , script
like = script
print 'getting to know about you'
lives = raw_input(prompt)
print "do you love computers and programing"
yesno = raw_input(prompt)

print"""
\twe are serving from %s file,\n
\tabout you %s , \n
\tyou love programing %s,\n
""" %(like, lives, yesno)
