# a simple python textbased game.
# @linix 8:40 pm sunday 26 feb 17
#
#

print "you enter a dark room with two door.Do you go through door #1 or #2."

door = raw_input(">>")

if door == '1':
    print "There is giant bear there, eating a cheese cake. What do you do?"
    print "1:Take the cake"
    print '2:scream at the bear'

    bear = raw_input('>>')

    if bear == '1':
        print "The bear eats off your face.Good job!!"
    elif bear == '2':
        print "The bear eats off your legs off.Good job!!"
    else:
        print "It is probally better the bear runs off."

#second door
elif door == '2':
    print "you got two boxes , a blue saphire box and a golden shiny box.What do you do?"
    print "1:you open the blue box."
    print "2:you open the golden box"

    box = raw_input('>>')

    if box == '1':
        print "you were sucked like a vacume inside it."
    elif box == '2':
        print "you got a way to the infinite treasure"
    else:
        print "you got a way back to home!!"
else:
    print 'no door are opened'
