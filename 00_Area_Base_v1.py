'''
programme to calculate area and perimeter if different shapes
v1 - set up the skeleton of the program
M.M - 16 June 2022
'''

# Import library
import random as r

# Functions

#Getting the shape name and make sure it is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response !="":
            return response
        else:
            print("Sorry, this can't be blank. "
                  "Please enter a shape name!")

# Check if integer is valid (must be positive whole numbers)
def int_checker():
    print("placeholder")

# String checker
def string_checker(list_of_allowable):
    print("place holder")

# Addition function
def square():
    print("place holder")

# Subtraction function
def triangle():
    print("place holder")

# Multiplication function
def rectangle():
    print("place holder")

# Division function
def circle():
    print("place holder")


# Set up lists and constants
answer_list = []
yes_no_list = [["yes", "y"], ["no", "n"]]
operands = ["+", "-", "*", "/"]


# Main routine
print("placeholder")

# Checking that shape name is not blank
shape = not_blank("Shape: ")

# Get dimensions of shape

# Calculations

# Print Area and Perimeter of shape


