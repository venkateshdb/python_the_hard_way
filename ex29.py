#python script
#
#11:29 pm wednesday @linix
#
# use of if statements

people = 20
cats = 30
dogs = 15

#use of if statements
if people < cats:
    print "too many cats! the world is doomed!"

if people > cats:
    print "not too many cats, world is saved!"

if people < dogs:
    print "the world is full of dogs"

if people > dogs:
    print "the world is full of humans!"

dogs += 5
if people >= dogs:
    print "people are greater than or equal to dogs"

if people <= dogs:
    print "people are less than equal to dogs"

if people == dogs:
    print "people are dogs"

"""
what if statements does is that they check a certain condition
and if the condition meets the criteria the code that has to be
executed (indented ones) is processed.
"""
# use if and else statements
people += cats
if people > cats:
    print "cats is dying"
else:
    print "population is less"

if dogs == cats:
    print "dogs are equal to cat"
else:
    print "dogs are not equal to cats"

print dogs > people and cats < cats
print "logical statements goes here"

people = 20
cats = 30
dogs = 40
boo = people + cats > dogs *50 or people * 100 == people + cats > dogs *50

if people + cats > dogs *50 or people * 100 == people + cats > dogs *50:
    print "wow what is happening\n"
else:
    print 'opps!!!'

print boo
