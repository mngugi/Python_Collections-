import math

def euclidean_Distance(pt1, pt2):
    return math((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)



pt1 = (1,2)
pt2 = (4,6)

distance = euclidean_Distance(pt1, pt2)

print(f"The Euclidean Distance between {pt1} and {pt2} is {distance:.2f}")