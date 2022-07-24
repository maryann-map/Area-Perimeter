'''
component 7 version 3 - if they got it wrong then print the correct answer
                      - also edited the print statements
'''

# Area and Perimeter are set to 4 and 5 (testing purposes)
area = 5
perimeter = 4

# Ask user what area they got
user_area = int(input("What area did you get?"))

# if user got same answer as programme then say 'good job'
if user_area == area:
    print("Good Job! You got it right.")
# if they got wrong answer then print 'sorry that is wrong'
else:
    print("Sorry that is wrong. The correct answer is {}.".format(area))

# Ask user what perimeter they got
user_perimeter = int(input("What perimeter did you get?"))

# if user got same answer as programme then say 'good job'
if user_perimeter == perimeter:
    print("Good Job")
# if they got wrong answer then print 'sorry that is wrong'
else:
    print("Sorry that is wrong. The correct answer is {}".format(perimeter))
