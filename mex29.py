#python code
# 11:48 pm wed @linix
#truth table pratice code.

print "Lets test your logical understanding\nusing this truthtb test"
print '(^^USE LOWERCASE LETTERS ONLY!!!)'

print '*' * 20
print "\tLOGIC FOR AND"
print '*' * 20
#logic for AND
first1 = raw_input('what is the logic for TRUE and TRUE >>')
first2 = raw_input('what is the logic for TRUE and FALSE >>')
first3 = raw_input('what is the logic for FALSE and FALSE >>')
first4 = raw_input('what is the logic for FALSE and TRUE >>')

print '*' * 20
print "\tLOGIC FOR OR"
#logic for OR
second1 = raw_input('what is logic for TRUE or TRUE >>')
second2 = raw_input('what is the logic for FALSE or FALSE >>')
second3 = raw_input('what is the logic for TRUE or FALSE >>')
second4 = raw_input('what is the logic for FALSE or TRUE >>')

print '*' * 20
print "\tLOGIC FOR NOT"
#logic for NOT
third1 = raw_input('what is the logic for NOT TRUE >>')
third2 = raw_input('what is the logic for NOT FALSE >>')

#checking the answers.
if first1 == 'true':
    print "awesome!!"
else:
    print "need more pratice??"
    
if first2 == 'false':
    print 'well done!!'
else:
    print "BE focused "

if first3 == 'false':
    print 'good going'

if first4 == 'fasle':
    print "yepee!!"
else:
    print "ok!! need to stydy"
