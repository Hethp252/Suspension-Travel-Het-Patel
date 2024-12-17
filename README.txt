# Suspension Travel README

# Why I did this project:
I am a part of Terps Racing-Electronics and Testing team and we
create rally cars and compete with other colleges. I was tasked
to find the highest ground clearance we can have in the car.
I also tasked to measure how much the car leans when the car turns.
The suspension team will use the data I provided to make iteration
to the suspension by making it lighter and more durable.

# Data collection
* First, we installed a race capture device to the car then I added
a circuit board that I created which was connected to a string
potentiometer
* The string potentiometer measures the height.
* The height changes are recorded in volts so I had to create an
intial test which measured how much voltage is recorded in the
race capture which is how I found the equations that I used in the code.
*We drove the car on an obstacle course that my team created and the
race capture recorded the data.

# How the code operates
## Step one
* Type python suspension.travel.py rc_(any numbers between 0 and 6).csv
in any terminal to run the code.
## Step two
* The filename will be printed so the user knows that this is the correct file.
* The code will read the file with pandas.
* The code will use the an equation to make the data usable using pandas.
* The code will plot two graphs using matplotlib.pyplot


# Uses for this code

This code plots the suspension travel of a car in inches which allows
me to analyze how much the suspension travels which I can use
to see how much ground clearance there is.