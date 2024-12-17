# analog 1 = front left suspension
# analog 2 = front right suspension

# right suspension equation: 9.92x -14.2= Distance
# left suspension equation: 9.36x-12.2= Distance

# (in the equations above) x=volts

# x = "interval"
# y = "suspension travel (distance in inches)"

import pandas as pd
import sys
import matplotlib.pyplot as plt

# Only one file is selected at a time.
if len(sys.argv) < 2:
    sys.exit(1)

# Get the filename from terminal
filename = sys.argv[1]

# Print the filename to make sure it's the right file
print(f"File selected: {filename}")


# Reads the data csv file, extract travel data, and then analyzes useful values
df = pd.read_csv(filename)

# Converting large and weird named headings into more manageable names.
df = df.rename(columns= {'Interval|"ms"|0|0|1': "Interval", 
                        'Analog1|"Volts"|0.0|5.0|100': "Front left suspension", 
                        'Analog2|"Volts"|0.0|5.0|100': "Front right suspension"})

# All the data is converted into useful data using equations.
def calculate_travel_dist_time(df):
    df['Distance_left'] = 9.36 * df['Front left suspension'] - 12.2 # front left suspension.
    df['Distance_right'] = 9.92 * df['Front right suspension'] - 14.2 # front right suspension.
    df['Time (seconds)'] = df['Interval'] / 1000 # interval in ms is converted in seconds.
    return df

# Calling the function
df = calculate_travel_dist_time(df)

# Plots the data in the correct order.
df.plot.scatter(x= 'Time (seconds)', y='Distance_right', color = 'red')
df.plot.scatter(x= 'Time (seconds)', y='Distance_left', color = 'blue')
plt.show()