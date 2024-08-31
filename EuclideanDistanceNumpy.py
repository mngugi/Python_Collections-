import numpy as np 



def euclidean_Distance(pt1, pt2):
    return np.linalg.norm(np.array(pt1) - np.array(pt2))  

pt1 = (1, 2)
pt2 = (4, 6)

distance = euclidean_Distance(pt1, pt2)

print(f"The Euclidean Distance between {pt1} and {pt2} is {distance:.2f}")
