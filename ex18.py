#learning to use function.
def myfunc(*args): #using arguments same as in previous chapters
    arg1 , arg2 = args  # passing arguments
    print "first: {} second:{}" .format(arg1 , arg2)  #simple string.
myfunc("hello" , 2040) # now callling function for giving this arguments.
#rewriting a new function
def sec(*args):
    one , two = args
    print "%s____is a simple set of words,\n%s___command to output something on screen." %(one , two)
print "Q1)____is a simple set of words\n"
print "Q2)___command to output something on screen"
x = raw_input("ans1>>")
y = raw_input("ans2>>")
sec(x, y)
def print_alpha(sin , cos):
    print 'what is %s , and %s' % (sin,cos)
print_alpha('trigo' ,'values')
def sing(lol):  #makiing a functin , and assingg it a variable
    print 'what is past tense of sing is >> %s'  % lol #prit command
sing('sang') # callig the function
