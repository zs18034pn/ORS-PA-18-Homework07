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

    empty_list = {}
    length = len(given_list)
    number_of_appearance = 0

    for i in range(length):

        if given_list[i] not in empty_list:

            for number in range(i, length):
                if given_list[number] == given_list[i]:

                    number_of_appearance += 1

                given_number = given_list[i]

                empty_list[given_number] = number_of_appearance
        number_of_appearance = 0

    sequence = []

    for el in empty_list:

        sequence.append(empty_list[el])
    maximum = sequence[0]

    for i in range(len(sequence)):
        if sequence[i] > maximum:
            maximum = sequence[i]

    for el in empty_list:
        if maximum == empty_list[el]:
            return el


def main():

    example_list = [8, 4, 0, 2, 2, 2, 5, 7, 0, 9, 8, 33, -10, 20, 2]
    x = number_of_appearances(example_list)

    print("In the example list number that appears the most is : " + str(x))
    pass


if __name__ == "__main__":
    main()