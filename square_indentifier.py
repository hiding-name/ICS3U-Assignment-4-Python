#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Oct 2019
# This is program find if square


def main():
    # funciton calculates if shape is square based on dimensions

    # Welcome statement
    print("Welcome, using the width and length of a rectangle, I will tell you"
          " if it is also a square.")
    input("Press Enter to continue.\n")

    # input
    width = input("What is the width: ")
    length = input("What is the length: ")

    try:
        int_width = int(width)
        int_length = int(length)
    except Exception as error:
        # https://stackoverflow.com/questions/1483429/how-to-print-an-exception-
        #   in-python and https://docs.python.org/3/tutorial/errors.html
        #   ^^^ python "as"
        print("\nInvalid input.")
        print("\nThe following error occured:\n" + str(error))

    # process
    if int_width == int_length:
        # output
        print("\nYour shape, with dimensions " + width + "x" + length +
              ", is a square.")
    else:
        print("\nYour shape, with dimensions " + width + "x" + length +
              ", is not a square.")


if __name__ == "__main__":
    main()
