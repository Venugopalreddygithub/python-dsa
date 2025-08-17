from array import array
import numpy as np  

my_array = array('i')
print(my_array)

my_array1 = array('i', [1, 2, 3, 4])
print(my_array1)

numpy_array = np.array([], dtype=int)
print(numpy_array)
numpy_arra1 = np.array([1, 2, 3, 4])
print(numpy_arra1)

""" 
Time & Space complexity for Empty array: O(1)
Time & Space complexity for array with data: O(n)
"""