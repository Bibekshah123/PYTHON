
# Lab1  Exercise #9 (Part 1)
#
# A program to compute the two roots of a quadratic equation.
#
# Import the math module to access function "math.sqrt()".

import math

A = float( input( "\"Enter the coefficient A:\" " ) )

B = float( input( "\nEnter the coefficient B: " ) )

C = float( input( "\nEnter the coefficient C: " ) )

print( "\nThe coefficients of the equation are: " )
print( "  Coefficient A = ", A )
print( "  Coefficient B = ", B )
print( "  Coefficient C = ", C )


# ****Modify that program to compute the two roots of a quadratic equation, as described in the program comments. ****

d = (B*B-4*A*C)**(1/2)
root1 = (-B+d)/(2*A)  # replace 0.0 with the quadratic formula to calculate the roots
root2 = (-B-d)/(2*A)


print( "\nThe roots of the equation:\n" )
print( "  Root #1 = ", round(root1,2) )  # round the result to two decimal places before printing
print( "  Root #2 = ", round(root2,2) )