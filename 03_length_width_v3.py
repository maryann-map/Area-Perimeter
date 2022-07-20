'''
component 3 - asking for both width and length
v3 - get integers for length and width of shape (using functions)
'''

# code for length

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

        #if an integer is not entered, display error message
        except ValueError:
            print(error)

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

        #if an integer is not entered, display error message
        except ValueError:
            print(error)

# main routine goes here
length = length("Length:")
width = width("Width:")



