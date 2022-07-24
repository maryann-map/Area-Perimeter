'''
game to ask basic math questions
base component
v1 - set up the skeleton of the program
v2 - calling functions (tested, and it works)
v3 - adding in length & width functions (the functions are being called in the different shapes functions)
v4 - calculating the area and perimeter of each shape (I also replaced the length and width function with int_checker)
v5 - adding in string_checker & get_shape functions (include valid_shapes list)
   - also added in a 5th shape (parallelogram)
v6 - ask user what answer they got & compare with programmes answer (code in each shape function)
v7 - summary of chosen shapes and their answers displayed in a table format
'''

# Import library
import math
import pandas as pd

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
    all_shapes.append("Square")

    # Asking user for the sides of shape
    length = int_checker("What is the length?")
    width = int_checker("What is the width?")

    # Calculating Area
    area = length * width
    round_area = round(area, 2)
    area_sum.append(round_area)

    # Calculating Perimeter
    perimeter = (2*length) + (2*width)
    round_perimeter = round(perimeter, 2)
    perimeter_sum.append(round_perimeter)

    user_area = int(input("What area did you get?"))

    # if user got same answer as programme then say 'good job'
    if user_area == area:
        print("Good Job! You got it right.")
    # if they got wrong answer then print 'sorry that is wrong'
    else:
        print("Sorry that is wrong. The correct answer is {:.2f}.".format(area))

    user_perimeter = int(input("What perimeter did you get?"))

    # if user got same answer as programme then say 'good job'
    if user_perimeter == perimeter:
        print("Good Job! You got it right.")
    # if they got wrong answer then print 'sorry that is wrong'
    else:
        print("Sorry that is wrong. The correct answer is {:.2f}".format(perimeter))


# Triangle function
def triangle():
    print("Triangle")
    all_shapes.append("Triangle")

    side1 = int_checker("What is the length of side1?")
    side2 = int_checker("What is the length of side2?")
    height = int_checker("What is the height?")
    base = int_checker("What is the base?")

    # Calculating Area
    area = (base / 2) * height
    round_area = round(area, 2)
    area_sum.append(round_area)

    # Calculating Perimetr
    perimeter = side1 + side2 + base
    round_perimeter = round(perimeter, 2)
    perimeter_sum.append(round_perimeter)

    user_area = int(input("What area did you get?"))

    # if user got same answer as programme then say 'good job'
    if user_area == area:
        print("Good Job! You got it right.")
    # if they got wrong answer then print 'sorry that is wrong'
    else:
        print("Sorry that is wrong. The correct answer is {:.2f}.".format(area))

    user_perimeter = int(input("What perimeter did you get?"))

    # if user got same answer as programme then say 'good job'
    if user_perimeter == perimeter:
        print("Good Job! You got it right.")
    # if they got wrong answer then print 'sorry that is wrong'
    else:
        print("Sorry that is wrong. The correct answer is {:.2f}".format(perimeter))


# Rectangle function
def rectangle():
    print("Rectangle")
    all_shapes.append("Rectangle")

    length = int_checker("What is the length?")
    width = int_checker("What is the width?")

    # Calculating Area
    area = length * width
    round_area = round(area, 2)
    area_sum.append(round_area)

    # Calculating Perimeter
    perimeter = (2*length) + (2*width)
    round_perimeter = round(perimeter, 2)
    perimeter_sum.append(round_perimeter)

    user_area = int(input("What area did you get?"))

    # if user got same answer as programme then say 'good job'
    if user_area == area:
        print("Good Job! You got it right.")
    # if they got wrong answer then print 'sorry that is wrong'
    else:
        print("Sorry that is wrong. The correct answer is {:.2f}.".format(area))

    user_perimeter = int(input("What perimeter did you get?"))

    # if user got same answer as programme then say 'good job'
    if user_perimeter == perimeter:
        print("Good Job! You got it right.")
    # if they got wrong answer then print 'sorry that is wrong'
    else:
        print("Sorry that is wrong. The correct answer is {:.2f}".format(perimeter))


# Circle function
def circle():
    print("Circle")
    all_shapes.append("Circle")

    # Ask user for radius of circle
    radius = int_checker("What is the Radius?")

    # Calculating Area pie r 2
    area = math.pi * radius * radius
    round_area = round(area, 2)
    area_sum.append(round_area)

    # Calculating Perimeter 2 pie r
    perimeter = 2 * math.pi * radius
    round_perimeter = round(perimeter, 2)
    perimeter_sum.append(round_perimeter)

    user_area = int(input("What area did you get?"))

    # if user got same answer as programme then say 'good job'
    if user_area == area:
        print("Good Job! You got it right.")
    # if they got wrong answer then print 'sorry that is wrong'
    else:
        print("Sorry that is wrong. The correct answer is {:.2f}.".format(area))

    user_perimeter = int(input("What perimeter did you get?"))

    # if user got same answer as programme then say 'good job'
    if user_perimeter == perimeter:
        print("Good Job! You got it right.")
    # if they got wrong answer then print 'sorry that is wrong'
    else:
        print("Sorry that is wrong. The correct answer is {:.2f}".format(perimeter))


# Parallelogram function (para = short form to prevent spelling errors)
def para():
    print("Parallelogram")
    all_shapes.append("Parallelogram")

    # Asking user for the sides of shape
    base = int_checker("What is the base?")
    height = int_checker("What is the height?")
    side = int_checker("What is length of side?")

    # Calculating Area
    area = base * height
    round_area = round(area, 2)
    area_sum.append(round_area)

    # Calculating Perimeter
    perimeter = 2 * (base + side)
    round_perimeter = round(perimeter, 2)
    perimeter_sum.append(round_perimeter)

    user_area = int(input("What area did you get?"))

    # if user got same answer as programme then say 'good job'
    if user_area == area:
        print("Good Job! You got it right.")
    # if they got wrong answer then print 'sorry that is wrong'
    else:
        print("Sorry that is wrong. The correct answer is {:.2f}.".format(area))

    user_perimeter = int(input("What perimeter did you get?"))

    # if user got same answer as programme then say 'good job'
    if user_perimeter == perimeter:
        print("Good Job! You got it right.")
    # if they got wrong answer then print 'sorry that is wrong'
    else:
        print("Sorry that is wrong. The correct answer is {:.2f}".format(perimeter))


# Main Routine


# valid options for yes / no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# List to store all the chosen shapes
all_shapes = []


# List to store the area of each shape (sum = summary)
area_sum = []

# List to store the perimeter of each shape (sum = summary)
perimeter_sum = []

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

df = pd.DataFrame(list(zip(all_shapes, area_sum, perimeter_sum)), columns=['Shape', 'Area', 'Perimeter'])
df = df.set_index('Shape')

print(df)


print()
print("Finish")
