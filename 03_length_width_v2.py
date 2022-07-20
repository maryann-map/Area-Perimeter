'''
component 3 - asking for both width and length
v1 - get integers for length and width of shape (using if statements)
'''

# code for length
try:
    error = ("Please enter a valid integer")

    length = int(input("Length: "))
    if length <= 0:
        print(error)
        length = int(input("Length: "))
    else:
        print(length)

except ValueError:
    print(error)

else:
    width = int(input("Width: "))
    if width <= 0:
        print(error)
        width = int(input("Width: "))
    else:
        print(width)


#main routine



