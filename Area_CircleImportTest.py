
# Script Name: Area_CircleImportTest.py
# Author: Mwangi
# Purpose: This script Calculates the area of a circle.
# The program tests Area_Circle module
# Usage: For example the expected outcome is :
#
# Area of the circle with radius 3: 28.27 square meters
# Surface area of the cylinder with radius 3 and height 5: 150.80 square meters
#

# Import the module Area_Circle

import Area_Circle

# Use the functions defined in Area_Circle

radius = 3
height = 5

# Calculate area using imported functions
circle_area = Area_Circle.calculate_circle_area(radius)
cylinder_area = Area_Circle.calculate_cylinder_area(radius, height)

# Print the results
print(f"Area of the circle with radius {radius}: {circle_area:.2f} square meters")
print(f"Surface area of the cylinder with radius {radius} and height {height}: {cylinder_area:.2f} square meters")

