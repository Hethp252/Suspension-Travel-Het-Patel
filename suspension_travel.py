# analog 1 = front left suspension
# analog 2 = front right suspension

# (in the equations) x=volts

# right suspension equation: 9.92x -14.2= Distance
# left suspension equation: 9.36x-12.2= Distance


# x = "interval"
# y = "suspension travel (distance in inches)"
import pandas as pd
import argparse
import matplotlib.pyplot as plt

# define arguments
# change this part
parser = argparse.ArgumentParser(description="View RaceCapture suspension travel data")
parser.add_argument('filename')
args = parser.parse_args()

# Reads the data csv file, extract travel data, and then analyzes useful values
df = pd.read_csv(args.filename)

# Converting large and weird named headings into more manageable names.
df = df.rename(columns= {'Interval|"ms"|0|0|1': "Interval", 
                        'Analog1|"Volts"|0.0|5.0|100': "Front left suspension", 
                        'Analog2|"Volts"|0.0|5.0|100': "Front right suspension"})

# All implementation of the equations in the data.
def calculate_travel_dist_time(df):
    # make a function for this part
    df['Distance_left'] = 9.36 * df['Front left suspension'] - 12.2 # front left suspension.
    df['Distance_right'] = 9.92 * df['Front right suspension'] - 14.2 # front right suspension.
    df['Time (seconds)'] = df['Interval'] / 1000 # interval in ms is converted in seconds.
    return df

df = calculate_travel_dist_time(df)

# plots the data
df.plot.scatter(x= 'Time (seconds)', y='Distance_right', color = 'red')
df.plot.scatter(x= 'Time (seconds)', y='Distance_left', color = 'blue')
plt.show()