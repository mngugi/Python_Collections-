import numpy as np
from scipy import stats
print ("Mean number is :")
x = np.mean([89,12,36,45,65,78])
print(x)

print ("Geometric Mean number is :")
g = stats.gmean([89,12,36,45,65,78])
print(g)

print ("Harmonic Mean number is :")
n = stats.hmean([89,12,36,45,65,78])
print(n)