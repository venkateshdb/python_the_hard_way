# using functions and return statements.
# @ ubutun
# python 2.7.13 @11.59 19/2/17
print "today we are going to use functions and return statements"
#so lets start
#defining a function
def call(name,age,hobbies):
    text = str(name)
    number = int(age)
    m_text = str(hobbies)
    return text , number , m_text

def sqt(x,y):
    var1 = int(x)
    var2 = int(y)
    return x * y

#using first function
name = raw_input('name>>')
age = raw_input('age>>')
hooby = raw_input('hobby>>')
# calling first function
value1 = call(name,age,hooby)
print value1
# second function goes here
var1 = int(raw_input('first no.'))
var2 = int(raw_input('second no.'))
#calling second function
value2 = sqt(var1,var2)
print 'value after multiplying is', value2
