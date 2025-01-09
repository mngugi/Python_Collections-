import math
import pyfiglet # type: ignore

def display_title(title):
    ascii_art = pyfiglet.figlet_format(title)
    print(ascii_art)

if __name__ == "__main__":
    display_title("Ball Angle")

horizontalPosition = 10
verticalPosition = 10

angle = math.atan(horizontalPosition / verticalPosition)

ballAngle = (angle / math.pi) * 180

print(ballAngle)
