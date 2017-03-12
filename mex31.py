# more elif statements @linix 9:10 pm sun 26 feb 17
#
#

print "Lets play a guessing game"

print "The game contains 10 numbers between 1-10.\n you have to guess the correct number.", "so lets play"

print "What you think the number is?"
num = 7
num1 = int(raw_input('>>'))
if num1 == 1:
    print "opps you are too far!"
    
elif num1 == 3:
        print "keep"

elif num1 == 5:
     print "Good try,Keep Going"

elif 5 < num1 < 7 :
    print "you are bit close,keep trying"

elif num1 in range(9,10):
     print "too far"

elif num1 == num:
     print "yupee well done!"

else:
     print "no "
