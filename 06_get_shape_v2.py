'''
component 6 v2 - asking user for a shape (contains lists of valid shape names)
using multiple if statements to check that valid_shape names is working for each shape
'''

# function goes here


def string_check(choice, options):
    for var_list in options:

        # if the snack is in one of the lists, return the full response
        if choice in var_list:

            # get full name of snack and put it
            # in title case it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the snack is not OK - ask question again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


# Get list of snacks
def get_shape():

    # valid snacks holds list of all snacks
    # Each item in valid snacks is a list with
    # valid options for each snack <full name, letter code (a -e),
    # and possible abbreviations etc.>

    valid_shapes = [
        ["circle", "c", "cir"],
        ["square", "s", "squ"],  # first item is square
        ["rectangle", "r", "rec"],
        ["triangle", "t", "tri"]
    ]

    desired_shape = ""
    while desired_shape != "xxx":

        # ask user for desired snack and put it in lowercase
        desired_shape = input("Shape: ").lower()

        if desired_shape == "circle":
            print("circle")
        elif desired_shape == "c":
            print("circle")
        elif desired_shape == "cir":
            print("cir")
        elif desired_shape == "square":
            print("square")
        elif desired_shape == "s":
            print("square")
        elif desired_shape == "squ":
            print("square")
        elif desired_shape == "rectangle":
            print("rectangle")
        elif desired_shape == "r":
            print("rectangle")
        elif desired_shape == "rec":
            print("rectangle")
        elif desired_shape == "triangle":
            print("triangle")
        elif desired_shape == "t":
            print("triangle")
        elif desired_shape == "tri":
            print("triangle")
        elif desired_shape == "xxx":
            break
        else:
            desired_shape = desired_shape

        # remove white space around snack
        desired_shape = desired_shape.strip()

        # check if snack is valid
        shape_choice = string_check(desired_shape, valid_shapes)


# Main routine goes here


# valid options for yes / no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# ask user if they are ready to pick a shape
check_shape = "invalid choice"
while check_shape == "invalid choice":
    want_shape = input("Ready to pick a shape?").lower()
    check_shape = string_check(want_shape, yes_no)
    if want_shape not in "yes_no":
        print("Please enter yes or no.")
    elif want_shape == "no" or want_shape == "n":
        break

# if they say yes, ask what shape they want (and save it in shape wanted list)
if check_shape == "Yes":
    get_shape()

else:
    chosen_shape = []

# show snack orders
print()
print("Finish")
