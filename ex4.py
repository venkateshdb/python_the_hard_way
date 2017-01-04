#now introducing important part of any pg lang.
#thats variables.
# for defining variables in pyhton we just us an assignment(=)
print 'there are some convention for defining a variable'
print """
they are:
1) variable name should start with a letter , no numbers or special characters are allowed.
2)aftre starting with no you can use any of them
3)use undrescore(_) while using space in between the variable.
"""
cars = 100
space_in_car = 7
passengers = 50
drivers = 70
cars_not_driven = cars - drivers
cars_driven = drivers
carpoll_capacity = cars_driven * space_in_car
average_passengers = cars_driven / passengers

# ok we have defined all variables. lets use them
print 'ok,python how many cars we are having'
print 'sir we have ' ,cars, " available"
print 'whats the capacity in cars' , space_in_car
print 'whats the number of passengers' , passengers
print 'and how many drivers'
print 'we have' ,drivers, "drivers"
print 'so by simple logic total available cars are' , cars_driven
print 'carpoll_capacity is' , carpoll_capacity
print 'average_passengers capacity' ,average_passengers
print 'it seems good lets go for the ride'
