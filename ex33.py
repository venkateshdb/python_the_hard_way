#python @linix 7:52 pm mon 27 feb 17
# using while loops
#

i = 0
numbers = []

while i <= 10:
    print "at the to i id %d" % i
    numbers.append(i)

    i += 1
    print "number now "  , numbers
    print "numbers at bottom i is %d " % i

print "the numbers"
for num in numbers:
    print num
