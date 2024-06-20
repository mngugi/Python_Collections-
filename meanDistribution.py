
import matplotlib.pyplot as plt

X = [32,62,83,45,96,83,74,65,45,96,21,85,74,25]
N = 14

sum_X = sum(X)
X_u = sum_X/N

print("Mean is: ", X_u)



plt.hist(X, bins=10, edgecolor='orange')

plt.xlabel('vlaues')
plt.ylabel('Frequency')

plt.show()
