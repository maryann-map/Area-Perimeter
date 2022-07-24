'''
component 6 v4 - asking user for a shape (contains lists of valid shape names)
trying nested list skills to check that valid_shape name responds to each shape

'''

# function goes here


# String checker
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
        ["circle", "c", "cir"],
        ["square", "s", "squ"],  # first item is square
        ["rectangle", "r", "rec"],
        ["triangle", "t", "tri"]
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
            print("circle")
        elif shape_choice == "Square":
            print("square")
        elif shape_choice == "Triangle":
            print("triangle")
        elif shape_choice == "Rectangle":
            print("rectangle")

# Main routine goes here


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
