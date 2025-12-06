# Problem set 0
# Assignment:
# Write a program that does the following in order:
    # 1. Asks the user to enter a number “x”
    # 2. Asks the user to enter a number “y”
    # 3. Prints out number “x”, raised to the
    # 4. Prints out the log (base 2) of “x”.

import numpy

x = int(input("Enter number x:"))

y = int(input("Enter number y:"))

res_pow = x**y
print(f"x**y = {res_pow}")

res_log = numpy.log2(x)
print(f"log(x) = {res_log}")