# python file @sunday linix @3:16 feb 26
#
# using if else and elif statements
#
"""
using my own function lists $see functions.py for more help
for now pr only handels 1 print commands.
"""

# importing module

import functions as easy

#making a simple userlogin code.
username = str(easy.inp('username >>'))
password = easy.inp('password >>')

if username == 'venky' and password == 'wecode':
    print"\n"
    easy.pr('*' * 50)
    print('welcome to shuttle service admin control screen, %s ') % username
    print '*' * 50
    buses = int(raw_input('NO OF BUSES>>'))
    pasangers = int(raw_input('NO OF PASSANGERS >>'))
    capacity = int(float(raw_input('CAPACITY OF VEHICLE >>')))
    capacity *= buses
    if capacity > pasangers:
        #print the input data on the screen
        print 'we have %d buses, %d pasangers and vehicle with %d pasangers per vehicle capacity' %(buses,pasangers,capacity)

       
    elif capacity == pasangers:
        print "OK!! BUSES fully occupied!!!"
    else:
        easy.pr('insufficient capacity!!')



else:
    print "\tintruder!!!"
#hacking into your system is very easy shuttle service haaa!!
