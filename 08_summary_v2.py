'''
component 8 version 2 - Adding in data frame
'''

# All data in the lists are for testing purposes

# Import Panda package
import pandas as pd

# List to store all the chosen shapes
all_shapes = ['Circle', 'Square', 'Triangle', 'Parallelogram', 'Rectangle']

# List to store the area of each shape
area = ['3', '4', '5', '6', '7']

# List to store the perimeter of each shape
perimeter = ['7', '6', '5', '4', '3']

# Table that has chosen shapes and its calculations
df = pd.DataFrame(list(zip(all_shapes, area, perimeter)), columns=['Shape', 'Area', 'Perimeter'])

# Print Table
print(df)
