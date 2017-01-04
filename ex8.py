#print '{} ' .format(1)
#print '{:{align}{width}}'.format('test', align='^', width='10')
#print '{:.{prec}} = {:.{prec}f}'.format('Gibberish', 2.7182, prec=3)
#print '{:open-the-pod-bay-doors}'.format(HAL9000())
#above are some ex of new formated string in python
formatter =  "%r %r %r"
print formatter  %('hello' , 'hi' , 'bye')
print formatter %('apple' , 'mango' , 'banana')
print """
muliti line     
string
can be used to write multi line strings
"""
print formatter %(100+52,478,455)
