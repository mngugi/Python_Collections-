import math

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

    #create a function calculate_circle_area
    
def calculate_cylinder_area(radius, height):
    """Calculates the area of a cylinder.

    Args:
      radius: The radius of the cylinder in meters.
      height: The height of the cylinder in meters.

    Returns:
      The area of the cylinder in square meters.
    """

    pi = math.pi
    area = pi * radius ** 2 * height
    return area

if __name__ == "__main__":
    radius = 2
    height = 10
    circle_area = calculate_circle_area(radius)
    cylinder_area = calculate_cylinder_area(radius, height)
    total_area = circle_area + cylinder_area
    print(total_area)
