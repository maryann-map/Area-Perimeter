'''
component 3 - asking for both width and length
v1 - get integers for length and width of shape (using if statements)
'''

# code for length
try:
    error = "Please enter a valid integer"

    # Ask user for length
    length = int(input("Length: "))
    # If length is less than 0 then print error message
    if length <= 0:
        print(error)
        length = int(input("Length: "))
    else:
        print(length)

except ValueError:
    print()

else:
    # Ask user for width
    width = int(input("Width: "))
    # If width is less than 0 then print error message
    if width <= 0:
        print(error)
        width = int(input("Width: "))
    else:
        print(width)


# main routine
