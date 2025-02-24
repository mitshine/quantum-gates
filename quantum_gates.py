import numpy as np
import math

arr1 = np.array([[1, 1], [1, -1]])
result1 = np.multiply(arr1, (1/math.sqrt(2)))
#print("arr1: \n", arr1)
print("Hadamard Gate: \n", result1)

arr2 = np.array([[1, 0], [0, -1]])
result2 = arr2
#print("arr2: \n", arr2)
print("Z Gate: \n", result2)

arr3 = np.array([[0, -1j], [1j, 0]])
result3 = arr3
#print("arr3: \n", arr3)
print("Y Gate: \n", result3)

arr4 = np.array([[0, 1], [1, 0]])
result4 = arr4
#print("arr4: \n", arr4)
print("X Gate: \n", result4)