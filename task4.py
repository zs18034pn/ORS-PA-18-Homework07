"""
===================   TASK 4  ====================
* Name: Number of Appearances
*
* Write a function that will return which element
* of integer list has the greatest number of
* appearances in that list.
* In case that multiple elements have the same
* number of appearances return any.
*
* Note: You are not allowed to use built-in
* functions.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here


def number_of_appearances(given_list):
    maximum = given_list[0]
    max_rep = 1
    for i in given_list:
        if given_list.count(i) > max_rep:
            max_rep = given_list.count(i)
            maximum = i
    print("Number", maximum, "appeared", max_rep, "times")


def main():
    # Test your function here
    int_list = [1, 2, 2, 2, 3, 4, 5, 5, 5]
    number_of_appearances(int_list)
    pass


if __name__ == "__main__":
    main()
