#@linix 26 9:40 feb 17 , 6:51 pm monday 27 feb 17
#python code
#use of for loop and lists.

hairs = ['black', 'brown', 'red']
color = ['red','black','orange']
weight = [1,2,3,4]

the_count = [1,2,3,4,5]
fruits = ['apple', 'mango', 'apricots' , 'banana']
change = [1 , 'pennies' , 2 , 'dimes' , 3  , 'quaters']

#for loop goes here
for numbers in the_count:
    print "this is count %d" % numbers
"""
the thing after for is just a variable kind thing
"""

for fruit in fruits:
    print "this type of fruits %s" % fruit

for joker in change:
    print "I have got  %r" % joker

# we can also make an empty list and fill it later.
elements =[]
#like this using append method
for i in range(0 , 6 ):
    print "adding %d to list" % i
    elements.append(i)

for i in elements:
    print "elements are: %d" % i

print numbers , fruit , joker
"""
append is use to add things to list.
"""
