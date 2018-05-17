"""Create a program that reads two integers, a and b, from the user.Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b"""

from math import log10

def arithmetic():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    sm = a+b
    sub = a-b
    product = a*b
    quotient = a/b
    remainder = a%b
    log = log10(a)
    power = a**b



    print ("Sum of a and b is: %.2f \nDifference of a and b is: %.2f \nProduct of a and b is: %.2f"%(sm, sub, product))
    print("quotient: %.2f"% quotient)
    print("remainder: %.2f"% remainder)
    print("log: %.2f"% log)
    print("power: %.2f"% power)

arithmetic()
