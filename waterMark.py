import matplotlib.pyplot as plt

x = range(10)
y = [i**2 for i in x]


plt.plot(x,y)

plt.text(0.5,0.5, 'Stingo', alpha=0.3, fontsize=50, rotation=45,
         ha='center', va='center', transform = plt.gca().transAxes)

plt.show()

