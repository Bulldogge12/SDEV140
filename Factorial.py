"""
Program: Factorial
Author: Todd Duff
Class: SDEV140
Last Modified: 4/1/2022

This program will prompt the user to enter a non-negative number
and calculate the factorial of that number."""

factorial = 1
num = int(input("Please enter a non-negative number: "))
print("You entered the number", num, ".")
if num < 0:
    print("You must enter a number greater than zero!")
elif num == 0:
    print("The factorial of zero is one.")
else:
    for num in range(1, num + 1):
        factorial = factorial * num
        print(factorial)
