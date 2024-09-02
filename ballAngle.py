import math

horizontalPosition = 10
verticalPosition = 10

angle = math.atan(horizontalPosition / verticalPosition)

ballAngle = (angle / math.pi) * 180

print(ballAngle)
