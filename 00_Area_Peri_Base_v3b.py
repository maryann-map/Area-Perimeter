'''
game to ask basic math questions
base component
v1 - set up the skeleton of the program
v2 - calling functions (tested, and it works)
v3 - adding in length & width functions (functions are being called from the main routine)
'''

# Import library

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


# Get length of shape
def length(question):

    error = "Please enter a valid integer"

    valid = False
    while not valid:

        # ask user for number and check if it is valid
        try:
            length = int(input(question))

            if length <= 0:
                print(error)
            else:
                return length

        # If an integer is not entered, display error message
        except ValueError:
            print(error)


# Get width of shape
def width(question):

    error = "Please enter a valid integer"

    valid = False
    while not valid:

        # ask user for number and check if it is valid
        try:
            width = int(input(question))

            if width <= 0:
                print(error)
            else:
                return width

        # if an integer is not entered, display error message
        except ValueError:
            print(error)


# String checker
def string_checker(list_of_allowable):
    print("place holder")


# Square function
def square():
    print("square")


# Triangle function
def triangle():
    print("triangle")


# Rectangle function
def rectangle():
    print("rectangle")


# Circle function
def circle():
    print("circle")


# ****** Main Routine ******

# Set up directions / lists needed to hold data


# Start of loop

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
        length("Length:")
        width("Width:")
    elif shape == "triangle":
        triangle()
        length("Length:")
        width("Width:")
    elif shape == "rectangle":
        rectangle()
        length("Length:")
        width("Width:")
    elif shape == "circle":
        circle()
        length("Length:")
        width("Width:")
    elif "xxx":
        break
    else:
        print("Invalid")
    count += 1

# Get dimensions of shape

# Calculations

# Print Area and Perimeter of shape
