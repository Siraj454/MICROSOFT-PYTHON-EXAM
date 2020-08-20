import math 
age=21
print("my age is {:3d} years".format(-age))
#precedence rules
total=10/2*4%3+4
check=10/2**2
print("total is {:.2f}".format(total))
print("Checked precendce  {:2f}".format(check))
print(" total is {:.2f} and check is {:.2f}".format(total,check))
#formating outputs with modulo operator
print("i have %2d cats and %d dogs"%(6,4))
pi=round((math.pi))
print("value of pi is ",pi)