'''
game to ask basic math questions
base component
v1 - set up the skeleton of the program
v2 - calling functions (tested, and it works)
'''

# Import library

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
    print("square")

# Subtraction function
def triangle():
    print("triangle")

# Multiplication function
def rectangle():
    print("rectangle")

# Division function
def circle():
    print("circle")


# Set up lists and constants

# Main routine

#start of loop

# initialised loop so that it runs at least once
shape = ""
count = 0
MAX_SHAPES = 5

while shape !="xxx" and count < MAX_SHAPES:

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
    elif "xxx":
        break
    else:
        print("Invalid")
    count +=1

# Get dimensions of shape

# Calculations

# Print Area and Perimeter of shape



