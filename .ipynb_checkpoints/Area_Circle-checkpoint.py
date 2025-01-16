# Script Name: Area_Circle.py
# Author: Mwangi
# Purpose: This script Calculates the area of a circle.
# Usage: For example the expected outcome is :
#
# Circle Area: 12.57 square meters
# Cylinder Surface Area: 150.80 square meters
# Total Area: 163.36 square meters
#
# This program is subsequently used as a module for the program Area_CircleImportTest.py
import math
import pyfiglet # type: ignore

def display_title(title):
    ascii_art = pyfiglet.figlet_format(title)
    print(ascii_art)

if __name__ == "__main__":
    display_title("Area of Circle")
def calculate_circle_area(radius):
    """Calculates the area of a circle.

    Args:
      radius: The radius of the circle in meters.

    Returns:
      The area of the circle in square meters.
    """
    pi = math.pi
    area = pi * radius ** 2
    return area

def calculate_cylinder_area(radius, height):
    """Calculates the surface area of a cylinder.

    Args:
      radius: The radius of the cylinder in meters.
      height: The height of the cylinder in meters.

    Returns:
      The surface area of the cylinder in square meters.
    """
    pi = math.pi
    area = 2 * pi * radius * (radius + height)  # Corrected formula for surface area
    return area

if __name__ == "__main__":
    # Example code to run if this script is executed directly
    radius = 2
    height = 10
    circle_area = calculate_circle_area(radius)
    cylinder_area = calculate_cylinder_area(radius, height)
    total_area = circle_area + cylinder_area

    # print the results
    print(f"Circle Area: {circle_area:.2f} square meters")
    print(f"Cylinder Surface Area: {cylinder_area:.2f} square meters")
    print(f"Total Area: {total_area:.2f} square meters")
