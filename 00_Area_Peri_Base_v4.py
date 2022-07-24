'''
game to ask basic math questions
base component
v1 - set up the skeleton of the program
v2 - calling functions (tested, and it works)
v3 - adding in length & width functions (the functions are being called in the different shapes functions)
v4 - calculating the area and perimeter of each shape (I also replaced the length and width function with int_checker)
'''

# Import library
import math

# Functions


# Getting the shape name and make sure it is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry, this can't be blank. "
                  "Please enter a shape name!")


# Check that integer is valid
def int_checker(question):

    error = "Please enter a valid integer"

    valid = False
    while not valid:

        # ask user for number and check if it is valid
        try:
            num = float(input(question))

            if num <= 0:
                print(error)
            else:
                return num

        # if an integer is not entered, display error message
        except ValueError:
            print(error)


# String checker
def string_checker():
    print("place holder")


# Square function
def square():
    print("square")
    # Asking user for the sides of shape
    side1 = int_checker("What is the length?")
    side2 = int_checker("What is the width")

    # Calculating Area
    area = side1 * side2

    # Calculating Perimeter
    perimeter = (2*side1) + (2*side2)

    # Print area and perimeter
    print("Area & Perimeter: {:.2f} & {:.2f}".format(area, perimeter))


# Triangle function
def triangle():
    print("triangle")
    side1 = int_checker("What is the length of side1:")
    side2 = int_checker("What is the length of side2:")
    height = int_checker("What is the height:")
    base = int_checker("What is the base:")

    # Calculating Area
    area = (base / 2) * height

    # Calculating Perimetr
    perimeter = side1 + side2 + base

    # Print area and perimeter
    print("Area & Perimeter: {:.2f} & {:.2f}".format(area, perimeter))


# Rectangle function
def rectangle():
    print("rectangle")
    side1 = int_checker("What is the length?")
    side2 = int_checker("What is the width")

    # Calculating Area
    area = side1 * side2

    # Calculating Perimeter
    perimeter = (2*side1) + (2*side2)

    # Print are and perimeter
    print("Area & Perimeter: {:.2f} & {:.2f}".format(area, perimeter))


# Circle function
def circle():
    print("circle")
    # Ask user for radius of circle
    radius = int_checker("What is the Radius:")

    # Calculating Area pie r 2
    area = math.pi * radius * radius

    # Calculating Perimeter 2 pie r
    perimeter = 2 * math.pi * radius

    # Print area and perimeter
    print("Area & Perimeter: {:.2f} & {:.2f}".format(area, perimeter))


# Main Routine

# Set up directions / lists needed to hold data


# Start of loop

error_message = "Please enter a valid answer"

# initialised loop so that it runs at least once
shape = ""
count = 0
MAX_SHAPES = 5

while shape != "xxx" and count < MAX_SHAPES:

    # Get details...
    shape = not_blank("Shape: ")
    # Get shape name and print shape that is chosen
    if shape == "square":
        square()
    elif shape == "triangle":
        triangle()
    elif shape == "rectangle":
        rectangle()
    elif shape == "circle":
        circle()
    elif shape == "xxx":
        break
    else:
        print(error_message)
    count += 1


# Calculations

# Print Area and Perimeter of shape
