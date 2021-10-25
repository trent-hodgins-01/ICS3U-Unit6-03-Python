# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 10/25/2021
# This is the list_array program
# The program generates and displays 10 random numbers between 1-100
# The program then figures out and displays the smallest of the 10 numbers


import random


def smallest_number(list_of_numbers):
    # this function determines the smallest number in the array
    number_in_list = list_of_numbers[0]
    for last_number_in_list in list_of_numbers:
        if last_number_in_list < number_in_list:
            number_in_list = last_number_in_list

    return number_in_list


def main():
    # this function uses an array

    list_array = []
    answer = 0
    added_numbers = 0

    # input
    for loop_counter in range(0, 10):
        a_number = random.randint(1, 100)
        list_array.append(a_number)
        number = loop_counter + 1
        print("Random number {0} is {1}".format(number, a_number))
        added_numbers = added_numbers + a_number

    calculate = smallest_number(list_array)

    print("\nThe smallest number is {0}".format(calculate))

    print("\nDone.")


if __name__ == "__main__":
    main()
