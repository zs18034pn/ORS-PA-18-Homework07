"""
===================   TASK 1   ====================
* Name: Roll The Dice
*
* Write a script that will simulate rolling the
* dice. The script should fetch the number of times
* the dice should be "rolled" as user input.
* At the end, the script should print how many times
* each number appeared (1 - 6).
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Note: You can use `rand` module to simulate dice
* rolling.
===================================================
"""

# Write your script here
from random import randrange
n = int(input("How many times should the dice be rolled? "))

num1 = num2 = num3 = num4 = num5 = num6 = 0

for i in range(n):
    number = randrange(1,7)
    # print(number)

    if number == 1:
        num1 += 1
    if number == 2:
        num2 += 1
    if number == 3:
        num3 += 1
    if number == 4:
        num4 += 1
    if number == 5:
        num5 += 1
    if number == 6:
        num6 += 1

print(" Number 1 appeared", num1, "times\n", "Number 2 appeared", num2, "times\n", "Number 3 appeared", num3, "times\n"
      " Number 4 appeared", num4, "times\n", "Number 5 appeared", num5, "times\n", "Number 6 appeared", num6, "times\n")


# This solution will not work if the input is not a positive integer

