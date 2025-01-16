from numpy import linspace

import matplotlib.pyplot as plt
import pyfiglet # type: ignore

def display_title(title):
    ascii_art = pyfiglet.figlet_format(title)
    print(ascii_art)

if __name__ == "__main__":
    display_title("Ball Plot")

velocity = 5

gravity = 9.81

time = linspace(0, 1, 1001)

vertical = velocity*time - 0.5*gravity*time**2


plt.plot(time, vertical)
plt.title('Trajectory of the ball')
plt.xlabel('time (s)')
plt.ylabel('vertical (m) ')

plt.show()

