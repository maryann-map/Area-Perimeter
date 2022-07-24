'''
game to ask basic math questions
base component
v1 - set up the skeleton of the program
v2 - calling functions (tested, and it works)
v3 - adding in length & width functions (the functions are being called in the different shapes functions)
v4 - calculating the area and perimeter of each shape (I also replaced the length and width function with int_checker)
v5 - adding in string_checker & get_shape functions (include valid_shapes list)
   - also added in a 5th shape (parallelogram)
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


def string_check(choice, options):
    for var_list in options:

        # if the shape is in one of the lists, return the full response
        if choice in var_list:

            # get full name of shape and put it
            # in title case it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the shape is not OK - ask question again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


# Get list of shapes
def get_shape():

    # valid shapes holds list of all shapes
    # Each item in valid shapes is a list with
    # valid options for each shape <full name, letter code (a -e),
    # and possible abbreviations etc.>

    valid_shapes = [
        ["circle", "c", "cir", "1"],
        ["square", "s", "squ", "2"],  # first item is square
        ["rectangle", "r", "rec", "3"],
        ["triangle", "t", "tri", "4"],
        ["parallelogram", "p", "para", "5"]
    ]

    desired_shape = ""
    while desired_shape != "xxx":

        # ask user for the shape they want and put it in lowercase
        desired_shape = input("Shape: ").lower()

        # if user inputs xx then break loop
        if desired_shape == "xxx":
            break

        else:
            desired_shape = desired_shape

        # remove white space around shape
        desired_shape = desired_shape.strip()

        # check if shape is valid
        shape_choice = string_check(desired_shape, valid_shapes)
        if shape_choice == "Circle":
            circle()
        elif shape_choice == "Square":
            square()
        elif shape_choice == "Triangle":
            triangle()
        elif shape_choice == "Rectangle":
            rectangle()
        elif shape_choice == "Parallelogram":
            para()


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


# Square function
def square():
    print("Square")
    # Asking user for the sides of shape
    length = int_checker("What is the length?")
    width = int_checker("What is the width?")

    # Calculating Area
    area = length * width

    # Calculating Perimeter
    perimeter = (2*length) + (2*width)

    # Print area and perimeter
    print("Area: {:.2f}".format(area))
    print("Perimeter: {:.2f}".format(perimeter))


# Triangle function
def triangle():
    print("Triangle")
    side1 = int_checker("What is the length of side1?")
    side2 = int_checker("What is the length of side2?")
    height = int_checker("What is the height?")
    base = int_checker("What is the base?")

    # Calculating Area
    area = (base / 2) * height

    # Calculating Perimetr
    perimeter = side1 + side2 + base

    # Print area and perimeter
    print("Area: {:.2f}".format(area))
    print("Perimeter: {:.2f}".format(perimeter))


# Rectangle function
def rectangle():
    print("Rectangle")
    length = int_checker("What is the length?")
    width = int_checker("What is the width?")

    # Calculating Area
    area = length * width

    # Calculating Perimeter
    perimeter = (2*length) + (2*width)

    # Print are and perimeter
    print("Area: {:.2f}".format(area))
    print("Perimeter: {:.2f}".format(perimeter))


# Circle function
def circle():
    print("Circle")
    # Ask user for radius of circle
    radius = int_checker("What is the Radius?")

    # Calculating Area pie r 2
    area = math.pi * radius * radius

    # Calculating Perimeter 2 pie r
    perimeter = 2 * math.pi * radius

    # Print area and perimeter
    print("Area: {:.2f}".format(area))
    print("Perimeter: {:.2f}".format(perimeter))


# Parallelogram function (para = short form to prevent spelling errors)
def para():
    print("parallelogram")
    # Asking user for the sides of shape
    base = int_checker("What is the base?")
    height = int_checker("What is the height?")
    side = int_checker("What is length of side?")

    # Calculating Area
    area = base * height

    # Calculating Perimeter
    perimeter = 2 * (base + side)

    # Print area and perimeter
    print("Area: {:.2f}".format(area))
    print("Perimeter: {:.2f}".format(perimeter))

# Main Routine


# valid options for yes / no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# ask user if they are ready to pick a shape (start programme)
check_shape = "invalid choice"
while check_shape == "invalid choice":
    want_shape = input("Ready to pick a shape?").lower()
    check_shape = string_check(want_shape, yes_no)
    if want_shape not in "yes_no":
        print("Please enter yes or no.")
    elif want_shape == "no" or want_shape == "n":
        break

# if they say yes, ask what shape they want (and save it in chosen shape list)
if check_shape == "Yes":
    get_shape()

else:
    chosen_shape = []

print()
print("Finish")
