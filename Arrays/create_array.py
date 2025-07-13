import array 

my_arr = array.array('i', []) # Create an empty array of integers
print(my_arr)

my_arr = array.array('i', [1, 2, 3, 4, 5]) # Create an array with initial values
print(my_arr)

import numpy as np

np_arr = np.array([], dtype=int) # Create an empty NumPy array of integers
print(np_arr)
np_arr = np.array([1, 2, 3, 4, 5]) # Create a NumPy array with initial values
print(np_arr)

""" 
Time complexity & Space complexity:
- Creating an empty array: O(1) time, O(1) space.
- Creating an array with initial values: O(n) time, O(n) space.
"""