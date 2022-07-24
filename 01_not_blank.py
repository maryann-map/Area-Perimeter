'''
component 1 - name not blank
v1 - If user does not enter something then repeat question
'''

# Functions go here


# Make sure that it is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry, this can't be blank. "
                  "Please enter a shape name!")


# Main routine goes here
shape = not_blank("Shape: ")
