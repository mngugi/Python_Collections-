import numpy as np
import time

def xarr():
    arry = np.arange(0, 9).reshape(3, 3)
    return arry

def yarr():
    yarr = np.ones((3, 3))
    return yarr

# Measure time for matrix multiplication using np.dot()
start_time = time.time()
xy = np.dot(xarr(), yarr())
end_time = time.time()
execution_time_np_dot = end_time - start_time

# Measure time for matrix multiplication using xarr.dot(yarr())
start_time = time.time()
xyi = xarr().dot(yarr())
end_time = time.time()
execution_time_dot = end_time - start_time

print("Matrix Product using np.dot():\n", xy)
print("\nMatrix Product using xarr.dot(yarr()) Function:\n", xyi)

print("\nExecution time using np.dot():", execution_time_np_dot, "seconds")
print("Execution time using xarr.dot(yarr()):", execution_time_dot, "seconds")
