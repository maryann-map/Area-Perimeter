'''
component 5 - calculating perimeter of shape
'''

# Ask user for sides of square
length = int(input("Length: "))
width = int(input("Width: "))

# Calculate perimeter by adding multiplying each side by 2 and then add them together
perimeter = (2*length) + (2*width)

# Show answer
print("Area: {}".format(perimeter))
