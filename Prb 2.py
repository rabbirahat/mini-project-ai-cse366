import matplotlib.pyplot as pt
import numpy as np

''' linspace in Python for creating numeric sequences. It's somewhat similar to the NumPy arrange function,
    in that it creates sequences of evenly spaced numbers structured as a NumPy array '''

x = np.linspace(-1000,1000)
y = np.linspace(-1000,1000)

'''meshgrid function is used to create a rectangular grid out of two given one-dimensional arrays 
   representing the Cartesian indexing or Matrix indexing.meshgrid function returns two 2-Dimensional arrays representing
   the X and Y coordinates of all the points. '''

x,y = np.meshgrid(x,y)

# plot the x and y axis
pt.axhline(0,xmin=0, xmax=1)  # will create horizontal line # pt.axhline() Add a horizontal line across the axis.
pt.axvline(0,ymin=0, ymax=1)  # will create vertical line

a = 72
b = 64

# plot hyperbolic equation
pt.contour(x,y,(y**2 / a**2 - x**2 / b**2),[1])

# add title on the graph
pt.title("Hyperbola Graph")

# display the plot
pt.show()