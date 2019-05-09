"""
===================   TASK 3  ====================
* Name: Insertion Sort
*
* Write a function that will implement insertion sort
* algorithm. Generate list of 1000 random integer
* numbers and sort the list using your function.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here


import random


def insertion_sort(list_of_ints):
    a = []
    while len(list_of_ints) >= 1:
        minimum = list_of_ints[0]
        for el in list_of_ints:
            if el < minimum:
                minimum = el

        a.append(minimum)
        list_of_ints.remove(minimum)

    return a

def main():
    # Test your function here
    example_list = []
    for i in range(0,1001):
        example_list.append(random.randint(0, 1000))

    print(insertion_sort(example_list))



if __name__ == "__main__":
    main()


