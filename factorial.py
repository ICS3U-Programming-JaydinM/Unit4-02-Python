#!/usr/bin/env python3

# Made by Jaydin Madore
# Made on 2022-11-01
# This program take the input of the user number and then tells the factorial of the integer


def main():

    # Tries to get the user_number as a positive integer.
    try:
        user_number = int(input("Enter a positive integer:"))
        print()
        # If the user does not enter a number
    except ValueError:
        print("You need to enter a positive integer.")
        main()
    # If the user enters a negative number it Restarts the program
    if user_number < 0:
        print("You need to enter a positive integer.")
        main()
    # Counter and factorial answer variables
    factorial_answer = 1
    counter = 0

    # This statement is used as a Do.. While
    while True:
        counter = counter + 1
        factorial_answer = factorial_answer * counter
        print("{} time through loop".format(counter))
        if counter >= user_number:
            break

    print()
    print("{}!={}".format(user_number, factorial_answer))


if __name__ == "__main__":
    main()
