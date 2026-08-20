'''data=[20,30,20,5,60,200,78,67]
for i in range(data[6],data[0],-1):
    print(i)



import numpy as np


# Generate 100 evenly spaced numbers between 0 and 10 (great for plotting)
x_coords = np.array(0, 10)

print(x_coords)

# Create a 3x3 matrix of all ones'''

#pip install pandas

import pandas as pd

# 1. Create a DataFrame from scratch (or read a file)
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}
df = pd.DataFrame(data)

# 2. View the table
print(df)
# Output:
#       Name  Age      City
# 0    Alice   25  New York
# 1      Bob   30    London
# 2  Charlie   35     Paris

# 3. Quickly calculate statistics on numerical columns
print(df['Age'].mean())  # Output: 30.0