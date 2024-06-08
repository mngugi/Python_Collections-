from numpy import linspace

import matplotlib.pyplot as plt

velocity = 5

gravity = 9.81

time = linspace(0, 1, 1001)

vertical = velocity*time - 0.5*gravity*time**2


plt.plot(time, vertical)
plt.xlabel('time (s)')
plt.ylabel('vertical (m) ')

plt.show()

