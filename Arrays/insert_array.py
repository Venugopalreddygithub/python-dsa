from array import array

# Insertion
my_array = array('i', [1, 2, 3, 4])
print(my_array)
my_array.insert(0, 6)
print(my_array)

""" 
Time Complexity: O(n)
Space Complexity: O(1)
"""
