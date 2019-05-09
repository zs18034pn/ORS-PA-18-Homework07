
"""
===================   TASK 2  ====================
* Name: Recursive Sum
*
* Write a recursive function that will sum given
* list of integer numbers.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here


def recursive_function(given_list):
    if not given_list:
        return 0

    return given_list[0] + recursive_function(given_list[1:])


def main():
    # Test your function here
    example_list = [2, 2, 3, 4, 5]
    print("The sum of the given list is: ", recursive_function(example_list))
    pass


if __name__ == "__main__":
    main()
