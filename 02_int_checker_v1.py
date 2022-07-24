'''
component 2 - integer checker function
v1 - checking to see that the function is called, returns value
'''

# Functions


# Check that valid integer was entered
def int_check():

    error = "Please enter a valid integer"

    valid = False
    while not valid:

        try:
            length = int(input("Length: "))
            if length <= 0:
                print(error)
            else:
                return length

        # if an integer is not entered, display error message
        except ValueError:
            print(error)


# main routine
int_check()
