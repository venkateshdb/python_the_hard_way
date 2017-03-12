print "lets practice everthing"
print "this\n is how \t escape characters \nwork"

poem ="\ta lovely world \n full of logic and beauty\n underneth itself\n some awesome secret\n and some adventurous things to \n be done  in this computers world"

print "--------------------------------------------"
print poem
print "--------------------------------------------"

ten = 20 * 10 - 190
print "This should be\t %d" % ten
def secret_formuls(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    carates = jars/ 1000
    return jelly_beans , jars , carates

starting_points = 1000
beans , jars , carates  = secret_formuls(starting_points)
print "with starting_points of this %d" % starting_points
print "we have jelly_beans:%d , jars:%d  , carates:%d" %(beans,jars,carates)
starting_points = starting_points /10
print "we can do it other way also"
print "we have jelly_beans:%d , jars %d, carates:%d" % secret_formuls(starting_points)
