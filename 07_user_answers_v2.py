'''
component 7 version 2 - asking user for their answers
'''

# Area and Perimeter are set to 4 and 5 (testing purposes)
area = 5
perimeter = 4

area_answer = int(input("What area did you get?"))

# if user got same answer as programme then say 'good job'
if area_answer == area:
    print("Good Job")
# if they got wrong answer then print 'sorry that is wrong'
else:
    print("Sorry that is wrong.")

perimeter_answer = int(input("What perimeter did you get?"))

# if user got same answer as programme then say 'good job'
if perimeter_answer == perimeter:
    print("Good Job")
# if they got wrong answer then print 'sorry that is wrong'
else:
    print("Sorry that is wrong.")
